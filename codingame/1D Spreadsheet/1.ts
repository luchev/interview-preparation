interface Cell {
    op: string;
    arg1: {
        type: string,
        val: number,
    };
    arg2: {
        type: string,
        val: number,
    };
};

const N: number = parseInt(readline());
let cells: Cell[] = [];
for (let i = 0; i < N; i++) {
    var inputs: string[] = readline().split(' ');
    const operation: string = inputs[0];
    const arg1: string = inputs[1];
    const arg2: string = inputs[2];
    cells.push({
        op: operation,
        arg1: {
            type: arg1.startsWith('$') ? 'REF' : 'VAL',
            val: parseInt(arg1.replace('$', ''))
        },
        arg2: {
            type: arg2.startsWith('$') ? 'REF' : 'VAL',
            val: parseInt(arg2.replace('$', ''))
        }
    });
}

function getVal(cells: Cell[], cell: Cell): number {
    // Resolve arguments
    if (cell.arg1.type === 'REF') {
        cell.arg1.val = getVal(cells, cells[cell.arg1.val]);
        cell.arg1.type = 'VAL';
    }

    if (cell.op !== 'VALUE' && cell.arg2.type === 'REF') {
        cell.arg2.val = getVal(cells, cells[cell.arg2.val]);
        cell.arg2.type = 'VAL';
    }

    // Handle the simple case when the operation is VALUE
    if (cell.op === 'VALUE') {
        return cell.arg1.val;
    }

    // Handle computation
    if (cell.op === 'ADD') {
        cell.arg1.val = cell.arg1.val + cell.arg2.val;
    } else if (cell.op === 'SUB') {
        cell.arg1.val = cell.arg1.val - cell.arg2.val;
    } else if (cell.op === 'MULT') {
        cell.arg1.val = cell.arg1.val * cell.arg2.val;
    }

    // Update cell status to value, because it's been computed
    cell.op = 'VALUE';

    // Handle javascript being retarded
    if (cell.arg1.val === -0) {
        cell.arg1.val = 0;
    }

    return cell.arg1.val;
}

for (let i = 0; i < N; i++) {
    console.log(getVal(cells, cells[i]));
}
