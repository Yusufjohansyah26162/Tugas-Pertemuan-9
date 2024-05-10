let numbers = [7, 4, 9, 2, 5, 1];

// Menghapus nilai-nilai yang ganjil
numbers = numbers.filter(num => num % 2 === 0);

// Mengurutkan nilai dari terkecil ke terbesar
numbers.sort((a, b) => a - b);

console.log(numbers);
