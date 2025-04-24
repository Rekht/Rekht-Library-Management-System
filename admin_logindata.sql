-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 05 Des 2023 pada 14.59
-- Versi server: 10.4.27-MariaDB
-- Versi PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `admin_logindata`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `admin_logindata`
--

CREATE TABLE `admin_logindata` (
  `ID` bigint(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `admin_logindata`
--

INSERT INTO `admin_logindata` (`ID`, `name`, `username`, `password`, `email`) VALUES
(21305141000, 'Admin 1', 'user', 'admin123', 'rekhtanggoro@gmail.com');

-- --------------------------------------------------------

--
-- Struktur dari tabel `list_books`
--

CREATE TABLE `list_books` (
  `id_book` bigint(20) NOT NULL,
  `judul` varchar(255) NOT NULL,
  `namapengarang` varchar(255) NOT NULL,
  `tahunterbit` int(4) NOT NULL,
  `genre` enum('Fantasy','Science Fiction','Mystery','Romance','Pendidikan') NOT NULL,
  `ketersediaan` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `list_books`
--

INSERT INTO `list_books` (`id_book`, `judul`, `namapengarang`, `tahunterbit`, `genre`, `ketersediaan`) VALUES
(7569, 'Buku 17', 'Pengarang 19', 1996, 'Science Fiction', 0),
(13031, 'Buku 15', 'Pengarang 6', 1992, 'Romance', 0),
(15361, 'Buku 3', 'Pengarang 3', 1996, 'Romance', 1),
(19445, 'Buku 19', 'Pengarang 20', 1995, 'Pendidikan', 1),
(20599, 'Buku 10', 'Pengarang 18', 2014, 'Mystery', 2),
(29286, 'Buku 5', 'Pengarang 7', 2018, 'Romance', 2),
(40309, 'Buku 11', 'Pengarang 11', 1991, 'Romance', 0),
(41525, 'Buku 3', 'Pengarang 8', 2006, 'Mystery', 1),
(42008, 'Buku 6', 'Pengarang 5', 1996, 'Mystery', 3),
(48142, 'Buku 15', 'Pengarang 6', 1996, 'Science Fiction', 3),
(56482, 'Buku 17', 'Pengarang 7', 1997, 'Science Fiction', 3),
(61482, 'Buku 11', 'Pengarang 14', 2018, 'Romance', 2),
(63882, 'Buku 2', 'Pengarang 11', 2001, 'Science Fiction', 3),
(65966, 'Buku 7', 'Pengarang 14', 1999, 'Mystery', 3),
(71306, 'Buku 13', 'Pengarang 20', 2017, 'Romance', 1),
(72144, 'Buku 4', 'Pengarang 13', 2006, 'Pendidikan', 2),
(75873, 'Buku 17', 'Pengarang 15', 1997, 'Fantasy', 3),
(83019, 'Buku 9', 'Pengarang 15', 2000, 'Mystery', 3),
(85401, 'Buku 15', 'Pengarang 20', 2010, 'Mystery', 3),
(94497, 'Buku 3', 'Pengarang 16', 2006, 'Science Fiction', 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `loan_book`
--

CREATE TABLE `loan_book` (
  `id_loan` bigint(18) NOT NULL,
  `tanggal_peminjaman` date NOT NULL,
  `tanggal_pengembalian` date NOT NULL,
  `denda` int(255) NOT NULL,
  `nim` bigint(11) NOT NULL,
  `id_book` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `member_logindata`
--

CREATE TABLE `member_logindata` (
  `nim` bigint(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `member_logindata`
--

INSERT INTO `member_logindata` (`nim`, `name`, `username`, `password`, `email`) VALUES
(21305141045, 'Restu Anggoro Kasih', '12345678', '12345678', 'rekhtanggoro@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `admin_logindata`
--
ALTER TABLE `admin_logindata`
  ADD PRIMARY KEY (`ID`);

--
-- Indeks untuk tabel `list_books`
--
ALTER TABLE `list_books`
  ADD PRIMARY KEY (`id_book`);

--
-- Indeks untuk tabel `loan_book`
--
ALTER TABLE `loan_book`
  ADD PRIMARY KEY (`id_loan`),
  ADD KEY `nim` (`nim`),
  ADD KEY `id_book` (`id_book`);

--
-- Indeks untuk tabel `member_logindata`
--
ALTER TABLE `member_logindata`
  ADD PRIMARY KEY (`nim`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `admin_logindata`
--
ALTER TABLE `admin_logindata`
  MODIFY `ID` bigint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21305141002;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `loan_book`
--
ALTER TABLE `loan_book`
  ADD CONSTRAINT `id_book` FOREIGN KEY (`id_book`) REFERENCES `list_books` (`id_book`),
  ADD CONSTRAINT `nim` FOREIGN KEY (`nim`) REFERENCES `member_logindata` (`nim`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
