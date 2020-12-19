const N: number = parseInt(readline()); // Number of elements which make up the association table.
const Q: number = parseInt(readline()); // Number Q of file names to be analyzed.
let extensionsTable = {};
for (let i = 0; i < N; i++) {
    var inputs: string[] = readline().split(' ');
    const EXT: string = inputs[0]; // file extension
    const MT: string = inputs[1]; // MIME type.
    extensionsTable[EXT.toLowerCase()] = MT;
}

for (let i = 0; i < Q; i++) {
    const FNAME: string = readline(); // One file name per line.
    let splitName = FNAME.split('.');
    if (splitName.length === 1) {
        console.log('UNKNOWN');
    } else {
        let extension = splitName[splitName.length - 1].toLowerCase();
        let mime = extensionsTable[extension];
        if (mime === undefined) {
            console.log('UNKNOWN');
        } else {
            console.log(mime);
        }
    }
}
