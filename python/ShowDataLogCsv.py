import csv
import re
import json

def parse_logs(log_file_path):
    extracted_data = []

    with open(log_file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        for row in reader:
            # Asegurémonos de tener al menos dos columnas: timestamp y message
            if len(row) < 2:
                continue

            timestamp = row[0]
            message = row[1]
            
            # Verificar si el mensaje contiene la cadena de autorización específica
            entry_data = {}

            # Extraer OrderCode del JSON response
            order_code_match = re.search(r'"OrderCode":(\d+)', message)
            if order_code_match:
                entry_data['OrderCode'] = order_code_match.group(1)

            # Extraer Tags - mejorado para capturar todos los formatos posibles
            tags_pattern = r'"Tags":\s*\[(.*?)\]'
            tags_match = re.search(tags_pattern, message, re.DOTALL)
            if tags_match:
                tags_text = tags_match.group(1).strip()
                
                # Si hay tags, procesarlos
                if tags_text:
                    # Manejar comillas dobles escapadas y separar por comas
                    tags = []
                    current_tag = ""
                    in_quotes = False
                    
                    for char in tags_text:
                        if char == '"' and (len(current_tag) == 0 or current_tag[-1] != '\\'):
                            in_quotes = not in_quotes
                            if not in_quotes and current_tag:  # Final de una etiqueta entrecomillada
                                tags.append(current_tag)
                                current_tag = ""
                        elif char == ',' and not in_quotes:
                            if current_tag:  # Agregar tag si hay algo
                                tags.append(current_tag.strip())
                            current_tag = ""
                        else:
                            current_tag += char
                    
                    # Agregar última etiqueta si quedó algo
                    if current_tag:
                        tags.append(current_tag.strip())
                    
                    # Limpiar comillas
                    tags = [tag.strip('"') for tag in tags]
                    entry_data['Tags'] = tags
                else:
                    entry_data['Tags'] = []

            # Extraer X-Viva-Correlationid de los Headers
            correlation_match = re.search(r'"X-Viva-Correlationid","Value":"([^"]+)"', message)
            if correlation_match:
                entry_data['X-Viva-Correlationid'] = correlation_match.group(1)

            # Buscar cualquier posible fecha de expiración en los tokens
            exp_match = re.search(r'"ExpirationDate":"([^"]+)"', message)
            if exp_match:
                epoch_time = exp_match.group(1)
                entry_data['ExpirationDate'] = epoch_time

            response_match = re.search(r'Data\.Response Content:\s*(\{.*\})', message, re.DOTALL)
            if response_match:
                try:
                    response_json = json.loads(response_match.group(1))
                    entry_data['response'] = response_json
                except json.JSONDecodeError:
                    entry_data['response'] = 'Error mapping JSON'

            # Si encontramos un OrderCode, agregamos esta entrada a nuestros resultados
            if 'OrderCode' in entry_data:
                entry_data['Timestamp'] = timestamp
                extracted_data.append(entry_data)

    return extracted_data

def main():
    log_file_path = 'log.csv'  # Actualiza con la ruta de tu archivo
    results = parse_logs(log_file_path)

    if results:
        print(f"{len(results)} log records found:")
        for idx, entry in enumerate(results, 1):
            print(f"\Record {idx}:")
            print(f"  Timestamp: {entry['Timestamp']}")
            print(f"  OrderCode: {entry.get('OrderCode', 'No Found')}")
            print(f"  Tags: {entry.get('Tags', [])}")
            print(f"  ExpirationDate: {entry.get('ExpirationDate', 'No Found')}")
            print(f"  X-Viva-Correlationid: {entry.get('X-Viva-Correlationid', 'No Found')}")
            print(f"  response: {json.dumps(entry.get('response', 'No Found'), indent=2)}")

        # Guardar los resultados en un archivo .txt
        with open('log_results.txt', 'w', encoding='utf-8') as output_file:
            for idx, entry in enumerate(results, 1):
                output_file.write(f"Record {idx}:\n")
                output_file.write(f"  Timestamp: {entry['Timestamp']}\n")
                output_file.write(f"  OrderCode: {entry.get('OrderCode', 'No Found')}\n")
                output_file.write(f"  Tags: {entry.get('Tags', [])}\n")
                output_file.write(f"  ExpirationDate: {entry.get('ExpirationDate', 'No Found')}\n")
                output_file.write(f"  X-Viva-Correlationid: {entry.get('X-Viva-Correlationid', 'No Found')}\n")
                output_file.write(f"  response: {json.dumps(entry.get('response', 'No Found'), indent=2)}\n")
                output_file.write("\n")

    else:
        print("No se encontraron registros de log que coincidan con el criterio de autorización.")

if __name__ == "__main__":
    main()

