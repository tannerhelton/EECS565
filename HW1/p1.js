const ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const KEY = "DAWN";
const CIPHERTEXT = "vealruwgwwk".toUpperCase();

var tmp = "";
for (var c in CIPHERTEXT) {
  var i =
    (ALPHABET.indexOf(CIPHERTEXT[c]) -
      ALPHABET.indexOf(KEY[c % KEY.length]) +
      ALPHABET.length) %
    ALPHABET.length;
  console.log(c);
  tmp += ALPHABET[i];
}
console.log(tmp);
