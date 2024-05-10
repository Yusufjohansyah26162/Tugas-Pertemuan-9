let numbers = [8, 3, 12, 4, 7, 2];

// Menghapus angka yang kurang dari 5 dan menggantikannya dengan 0
numbers = numbers.map(num => num < 5 ? 0 : num);

// Mengurutkan array dari nilai terbesar ke terkecil
numbers.sort((a, b) => b - a);

console.log(numbers);
