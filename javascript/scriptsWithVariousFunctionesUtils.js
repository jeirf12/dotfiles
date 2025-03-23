function prepareGifts(gifts) {
  return Array.from(new Set(gifts)).sort((a, b) => a - b);
}

function createFrame(names) {
  const nameMaxSize = names.reduce((max, name) => Math.max(max, name.length), 0);

  const border = `**${"*".repeat(nameMaxSize)}**`;

  const frameCreate = names
    .map(name => `* ${name}${" ".repeat(nameMaxSize - name.length)} *`)
    .join("\n")
  return `${border}\n${frameCreate}\n${border}`;
}

function organizeInventory(inventory) {
  return inventory.reduce((acc, { name, quantity, category }) => {
    acc[category] = acc[category] || {}
    const { [name]: existingQuantity = 0 } = acc[category];
    acc[category][name] = existingQuantity + quantity;
    return acc;
  }, {});
}

function createXmasTree(height, ornament) {
  const trunk = "#", space = "_";
  let treeCreated = [];

  let ornamentCount = 1;
  for (let h = 0; h < height; h++) {
    const padding = space.repeat(height - h - 1);
    treeCreated.push(`${padding}${ornament.repeat(ornamentCount)}${padding}`);
    ornamentCount += 2;
  }
  const trunkLine = space.repeat(height - 1) + trunk + space.repeat(height - 1);
  treeCreated.push(trunkLine, trunkLine);
  return treeCreated.join("\n");
}

function organizeShoes(shoes) {
  const sizeCount = {};
  const result = [];

  for(const { type, size } of shoes) {
    sizeCount[size] = sizeCount[size] || { I: 0, R: 0 }
    sizeCount[size][type]++;

    if (sizeCount[size].I > 0 && sizeCount[size].R > 0) {
      result.push(size);
      sizeCount[size].I--;
      sizeCount[size].R--;
    }
  }
  return result;
}

function inBox(box) {
  const character = "*";

  if (box[0].includes(character) || box[box.length - 1].includes(character)) return false;

  for(let i = 1; i < box.length - 1; i++) {
    if(/^(?!\*).*[^*]\*[^*].*$/.test(box[i])) {
      return true;
    }
  }

  return false;
}

function fixPackages(packages) {
  let current = '';
  let stack = [];
  for(const char of packages) {
    if (char === '(') {
      stack.push(current);
      current = '';
    } else if (char === ')') {
      current = stack.pop() + current.split('').reverse().join('');
    } else {
      current += char;
    }
  }
  return current;
}

function drawRace(indices, length) {
  const emptyTrack = "~".repeat(length);
  return indices
    .map((position, index) => {
      const renoPosition = ((position + length) % length);

      const track = renoPosition > 0 && renoPosition < length 
        ? emptyTrack.substring(0, renoPosition) + "r" + emptyTrack.substring(renoPosition + 1)
        : emptyTrack;

      return `${" ".repeat(indices.length - 1 - index)}${track} /${index + 1}`;
    }).join("\n")
}

function moveTrain(board, mov) {
  const resultMoves = {
    'o': 'crash',
    '·': 'none',
    '*': 'eat',
  };

  let head = board.findIndex(line => line.includes('@'));
  let position = board[head].indexOf('@');

  if(mov === 'U') {
    head--;
  } else if (mov === 'D') {
    head++;
  } else if (mov === 'L') {
    position--;
  } else if (mov === 'R') {
    position++;
  }

  const character = board[head]?.[position];
  return resultMoves[character === undefined ? 'o' : character];
}

function compile(instructions) {
  let values = {};
  let index = 0;
  while(index < instructions.length) {    
    const [cmd, value, key] = instructions[index].split(' ');
    if(!values[value]) values[value] = 0;

    if(cmd === 'MOV') {
      values[key] = values[value] || value;
    } else if (cmd === 'INC') {
      values[value]++;
    } else if (cmd === 'DEC') {
      values[value]--;
    } else if (cmd === 'JMP') {
      if(values[value] === 0) {
        index = key
        continue
      }
    }
    index++;
  }
  return values['A'];
}

function decodeFilename(filename) {
  const [namePart, extension] = filename.split(".")
  const namefile = namePart
    .replace(/(?:_|^)(-?\d+(\.\d+)?([eE][-+]?\d+)?)(?=_|$)/g, "")
    .replace(/^_|_$/g, "")

  return `${nameFile}.${extension}`;
}

function calculatePrice(ornaments) {
  const adornos = {
    "*": 1,
    "o": 5,
    "^": 10,
    "#": 50,
    "@": 100,
  }

  let total = 0;
  for (let i = 0; i < ornaments.length; i++) {
    const current = adornos[ornaments[i]];
    const next = adornos[ornaments[i + 1]];

    if(current === undefined) return undefined;

    total += (current < next ? -current : current)
  }

  return total;
}

