const ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const p = 3;
const q = 11;
const e = 7;
const n = p * q;
const phi = (p - 1) * (q - 1);
const d = 3;

const E = 5;
const C = 3;
const S = 19;

const encrypt = (m) => {
  return Math.pow(m, e) % n;
};

const decrypt = (c) => {
  return Math.pow(c, d) % n;
};

console.log(
  ALPHABET[encrypt(E)] +
    " " +
    ALPHABET[encrypt(E)] +
    " " +
    ALPHABET[encrypt(C)] +
    " " +
    ALPHABET[encrypt(S)]
);

console.log(
  ALPHABET[decrypt(14)] +
    " " +
    ALPHABET[decrypt(14)] +
    " " +
    ALPHABET[decrypt(9)] +
    " " +
    ALPHABET[decrypt(13)]
);
