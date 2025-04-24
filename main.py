from tkcalendar import *
from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox
from tkinter.ttk import Treeview
import random
import pymysql
import time
from datetime import date, timedelta
import mysql.connector
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Metode untuk mendapatkan dan mengubah ukuran gambar dengan pasti


def get_image_from_url(url, size=None):
    response = requests.get(url)
    img_data = BytesIO(response.content)
    img = Image.open(img_data)

    # Pastikan mengubah ukuran gambar dengan metode LANCZOS untuk kualitas lebih baik
    if size:
        img = img.resize(size, Image.Resampling.LANCZOS)

    # Konversi ke format yang kompatibel dengan Tkinter
    photo_img = ImageTk.PhotoImage(img)

    # Simpan referensi untuk mencegah garbage collection
    photo_img.image = img

    return photo_img


root = Tk()
root.iconbitmap('LibraryIcon.ico')

root.geometry("1000x562+200+80")
root.resizable(False, False)
root.title("Library Management System")

can = Canvas(root, bg="#6D93B1")
can.place(x=0, y=0, relwidth=1, relheight=1)

# URL gambar dari internet
calendar_url = "https://cdn-icons-png.flaticon.com/512/747/747310.png"
clock_url = "https://cdn-icons-png.flaticon.com/512/2088/2088617.png"

# Gunakan ukuran yang sangat kecil (12x12 pixels)
calanderimg = get_image_from_url(calendar_url, size=(12, 12))
clockimg = get_image_from_url(clock_url, size=(12, 12))

# Print untuk verifikasi
print(f"Calendar image size: {calanderimg.width()} x {calanderimg.height()}")
print(f"Clock image size: {clockimg.width()} x {clockimg.height()}")

# Lanjutkan dengan kode program Anda...


def loginbtnadmin():  # Login Button Function
    global user, passw, Admin_name, con, mycursor
    user = username.get()
    passw = password.get()
    if (user == "" or passw == ""):
        messagebox.showinfo(
            "Notification", "All fields are required", parent=root)
    elif (len(passw) < 8):
        messagebox.showerror(
            "Notification", "Password Must be of 8 Characters!!!", parent=root)
    else:
        try:
            con = pymysql.connect(
                host='localhost',
                user='root', password='ROOT')
            mycursor = con.cursor()
            query = 'use admin_logindata;'
            mycursor.execute(query)
            query = 'select * from admin_logindata where username=%s and password=%s;'
            t = mycursor.execute(query, (user, passw))
            if (t == True):
                root.withdraw()
                data = mycursor.execute(
                    "select name from admin_logindata where username=%s;", (user))
                data = mycursor.fetchall()
                for i in data:
                    Admin_name = i[0]
                adminlogin()
            else:
                messagebox.showerror('Notification', 'Incorrect Username or Password!!!\nPlease try again...',
                                     parent=root)
        except:
            messagebox.showerror(
                'Notification', 'Something is wrong!!!\nPlease try again...', parent=root)
            return


def loginbtnmember():  # Login Button Function
    global user, passw, Admin_name, con, mycursor
    user = username.get()
    passw = password.get()
    if (user == "" or passw == ""):
        messagebox.showinfo(
            "Notification", "All fields are required", parent=root)
    elif (len(passw) < 8):
        messagebox.showerror(
            "Notification", "Password Must be of 8 Characters!!!", parent=root)
    else:
        try:
            con = pymysql.connect(
                host='localhost',
                user='root',
                password='ROOT',)
            mycursor = con.cursor()
            query = 'use admin_logindata;'
            mycursor.execute(query)
            query = 'select * from member_logindata where username=%s and password=%s;'
            t = mycursor.execute(query, (user, passw))
            if (t == True):
                root.withdraw()
                data = mycursor.execute(
                    "select name from member_logindata where username=%s;", (user))
                data = mycursor.fetchall()
                for i in data:
                    Admin_name = i[0]
                adminlogin()
            else:
                messagebox.showerror('Notification', 'Incorrect Username or Password!!!\nPlease try again...',
                                     parent=root)
        except:
            messagebox.showerror(
                'Notification', 'Something is wrong!!!\nPlease try again...', parent=root)
            return


# Login Entry Boxes
username = StringVar()
password = StringVar()
# Login Frame Labels


def loginpagemember():
    titleLabel = Label(can, text='LOGIN SYSTEM', font=('Georgia', 20, 'italic bold'), bg='#6D93B1', fg='White', height=2,
                       relief='groove', bd=2)
    titleLabel.place(x=1, y=1, relwidth=1)

    can.create_image((430, 80), anchor='nw')

    can.create_text((370, 289), text="Username :",
                    font=('times', 15, 'italic bold'))

    can.create_text((370, 368), text="Password :",
                    font=('times', 15, 'italic bold'))

    usernameEntry = Entry(root, textvariable=username, width=25, font=(
        'times', 15, 'italic'), bd=5, bg='lightblue')
    usernameEntry.place(x=420, y=270)
    usernameEntry.focus()

    passwordEntry = Entry(root, width=25, show='*', textvariable=password,
                          font=('times', 15, 'italic'), bd=5, bg='lightblue')
    passwordEntry.place(x=420, y=350)

    # Login Submit Button
    loginbtn = Button(root, text='Login', font=('times', 13, 'italic bold'), bg='lightgreen', bd=5, activebackground='green',
                      activeforeground='white', command=loginbtnmember, width=8)
    loginbtn.place(x=590, y=410)

    login_as_admin_btn = Button(root, text='Login as Admin', font=('times', 9, 'italic bold'), bg='#76ABB6', fg='red', activebackground='#76ABB6',
                                activeforeground='#76ABB6', command=loginpageadmin, width=12)
    login_as_admin_btn.place(x=588, y=460)


def loginpageadmin():
    titleLabel = Label(can, text='LOGIN SYSTEM', font=('Georgia', 20, 'italic bold'), bg='#6D93B1', fg='White', height=2,
                       relief='groove', bd=2)
    titleLabel.place(x=1, y=1, relwidth=1)

    can.create_image((430, 80), anchor='nw')

    can.create_text((370, 289), text="Username :",
                    font=('times', 15, 'italic bold'))

    can.create_text((370, 368), text="Password :",
                    font=('times', 15, 'italic bold'))

    # Login Entry Boxes
    username = StringVar()
    password = StringVar()

    usernameEntry = Entry(root, textvariable=username, width=25, font=(
        'times', 15, 'italic'), bd=5, bg='lightblue')
    usernameEntry.place(x=420, y=270)
    usernameEntry.focus()

    passwordEntry = Entry(root, width=25, show='*', textvariable=password,
                          font=('times', 15, 'italic'), bd=5, bg='lightblue')
    passwordEntry.place(x=420, y=350)

    # Login Submit Button
    loginbtn = Button(root, text='Login as Admin', font=('times', 13, 'italic bold'), bg='lightgreen', bd=5, activebackground='green',
                      activeforeground='white', command=loginbtnadmin, width=12)
    loginbtn.place(x=550, y=410)


loginpagemember()


class ProfilePage(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.config(bg="#E5EACA")
        self.db_connection = self.connect_to_db()  # Koneksi SQL sebagai atribut

    def connect_to_db(self):
        # Metode untuk membuat koneksi ke database
        try:
            con = pymysql.connect(
                host='localhost', user='root', password='ROOT')
            return con
        except pymysql.Error as e:
            print(f"Error while connecting to the database: {e}")
            return None

    def fetch_profile_data(self):
        # Metode untuk mengambil data profil dari database
        if not self.db_connection:
            print("Database connection error.")
            return None

        try:
            with self.db_connection.cursor() as mycursor:
                query = 'use admin_logindata;'
                mycursor.execute(query)
                query = 'SELECT nim, name, username, password, email FROM member_logindata;'
                mycursor.execute(query)
                profile_data = mycursor.fetchone()  # Mengambil satu baris data profil
                return profile_data
        except pymysql.Error as e:
            print(f"Error while fetching profile data: {e}")
            return None

    def show_profile(self):
        profile_data = self.fetch_profile_data()

        profile_window = Toplevel(self.master)
        profile_window.geometry("450x300")
        profile_window.title("Profile Page")

        if profile_data:
            fields = [("Username:", profile_data[2]), ("Nama:", profile_data[1]),
                      ("Email:", profile_data[4]), ("NIM:", profile_data[0])]

            for label_text, entry_text in fields:
                Label(profile_window, text=label_text).pack()
                entry = Entry(profile_window)
                entry.insert(0, entry_text)
                entry.pack()
        else:
            error_label = Label(profile_window, text="Data tidak ditemukan")
            error_label.pack()


class Book:
    def __init__(self, id, judul, namapengarang, genre, tahunterbit, ketersediaan):
        self.id = id
        self.judul = judul
        self.namapengarang = namapengarang
        self.genre = genre
        self.tahunterbit = tahunterbit
        self.ketersediaan = ketersediaan

    # Fungsi details
    @staticmethod
    def details(tree):
        def get_books_from_database():
            try:
                con = mysql.connector.connect(
                    host='localhost', user='root', password='ROOT', database='admin_logindata')
                mycursor = con.cursor()
                query = 'SELECT id_book, judul, namapengarang, genre, tahunterbit, ketersediaan FROM list_books;'
                mycursor.execute(query)

                books = []
                for row in mycursor.fetchall():
                    id, judul, namapengarang, genre, tahunterbit, ketersediaan = row
                    books.append(Book(id,
                                      judul,
                                      namapengarang,
                                      genre,
                                      tahunterbit,
                                      ketersediaan))

                con.close()
                return books

            except mysql.connector.Error as e:
                print(f"Error: {e}")
                return []
        tree.delete(*tree.get_children())  # Hapus entri yang ada sebelumnya
        books = get_books_from_database()

        for book in books:
            tree.insert("", "end", values=(book.id, book.judul, book.namapengarang,
                        book.genre, book.tahunterbit, book.ketersediaan))

    @staticmethod
    def pinjam_book(tree):
        selected = tree.focus()  # Mendapatkan item yang dipilih di Treeview
        if selected:
            # Mendapatkan ID buku dari item yang dipilih
            book_id = tree.item(selected)['values'][0]
            try:
                con = mysql.connector.connect(
                    host='localhost', user='root', password='ROOT', database='admin_logindata')
                mycursor = con.cursor()

                # Mendapatkan ketersediaan buku dari database
                query_select = "SELECT ketersediaan FROM list_books WHERE id_book = %s"
                mycursor.execute(query_select, (book_id,))
                result = mycursor.fetchone()
                print(result)
                # Pastikan buku tersedia sebelum mengurangi ketersediaannya
                if result and result[0] > 0:
                    # Update ketersediaan buku di database
                    query_update = "UPDATE list_books SET ketersediaan = ketersediaan - 1 WHERE id_book = %s"
                    mycursor.execute(query_update, (book_id,))
                    con.commit()

                    # Tampilkan pesan bahwa buku berhasil dipinjam
                    loan_obj = Loan()  # Membuat objek dari kelas Loan

                    # Pemanggilan metode calculate_penalty
                    loan_obj.calculate_penalty()

                    # Kemudian, jika ingin memanggil metode tanggal_peminjaman setelah persetujuan buku oleh Admin
                    # Tambahkan kode berikut setelah menampilkan pesan "Buku telah disetujui oleh Admin"
                    messagebox.showinfo(
                        "Persetujuan", "Buku telah disetujui oleh Admin")
                    loan_obj.tanggal_peminjaman(tree, username, password)

                    # Perbarui tampilan Treeview dengan data yang diperbarui dari database
                    # Bersihkan isi Treeview sebelum diperbarui
                    tree.delete(*tree.get_children())

                    # Populate ulang Treeview dengan data yang diperbarui dari database
                    Book.details(tree)
                else:
                    messagebox.showwarning(
                        "Peringatan", "Buku tidak tersedia untuk dipinjam.")
            except mysql.connector.Error as e:
                print(f"Error: {e}")
                messagebox.showerror(
                    "Error", "Terjadi kesalahan saat meminjam buku.")
            finally:
                if con.is_connected():
                    mycursor.close()
                    con.close()

    @staticmethod
    def return_book(tree):
        try:
            # Membuat koneksi ke database MySQL
            conn = pymysql.connect(
                host='localhost',
                user='root',
                password='ROOT',
                database='admin_logindata'
            )

            cursor = conn.cursor()

            # Query untuk mendapatkan daftar buku yang dipinjam
            query = "SELECT * FROM loan_book"  # Sesuaikan dengan struktur database Anda
            cursor.execute(query)

            borrowed_books = cursor.fetchall()
            query = """
                SELECT loan_book.id_book, loan_book.tanggal_pengembalian, list_books.judul, list_books.namapengarang 
                FROM loan_book 
                JOIN list_books ON loan_book.id_book = list_books.id_book
            """
            cursor.execute(query)
            borrowed_books = cursor.fetchall()

            def return_book1(tree):
                selected = tree.focus()  # Mendapatkan item yang dipilih di Treeview
                if selected:
                    # Mendapatkan ID buku dari item yang dipilih
                    book_id = tree.item(selected)['values'][0]
                    try:
                        con = mysql.connector.connect(
                            host='localhost', user='root', password='ROOT', database='admin_logindata')
                        mycursor = con.cursor()

                        # Mengambil ID buku dari loan_book
                        query_book_id = "SELECT id_book FROM loan_book WHERE id_book = %s"
                        mycursor.execute(query_book_id, (book_id,))
                        # Mengambil ID buku yang sesuai
                        book_id = mycursor.fetchone()[0]
                        print(book_id)
                        # Mencari ketersediaan buku di list_books
                        query_select = "SELECT ketersediaan FROM list_books WHERE id_book = %s"
                        mycursor.execute(query_select, (book_id,))
                        # Mengambil ketersediaan buku
                        ketersediaan = mycursor.fetchone()[0]
                        print(ketersediaan)
                        if ketersediaan is not None:  # Jika buku ditemukan
                            # Hapus buku yang dipinjam dari tabel loan_book
                            query_delete = "DELETE FROM loan_book WHERE id_book = %s"
                            mycursor.execute(query_delete, (book_id,))
                            con.commit()
                            # Update ketersediaan buku di list_books
                            query_update = "UPDATE list_books SET ketersediaan = ketersediaan + 1 WHERE id_book = %s"
                            mycursor.execute(query_update, (book_id,))
                            con.commit()

                            loan = Loan()
                            total_denda = loan.calculate_penalty()
                            messagebox.showinfo(
                                "Pengembalian", f"Denda yang harus anda bayar sebesar : {total_denda}")

                            messagebox.showinfo(
                                "Pengembalian", "Buku berhasil dikembalikan!")

                            # Perbarui tampilan Treeview dengan data yang diperbarui dari database
                            # Bersihkan isi Treeview sebelum diperbarui
                            tree.delete(*tree.get_children())
                        else:
                            messagebox.showerror(
                                "Error", "Buku tidak ditemukan!")
                    except mysql.connector.Error as e:
                        print(f"Error: {e}")
                        messagebox.showerror(
                            "Error", "Terjadi kesalahan saat mengembalikan buku.")
                    finally:
                        mycursor.close()
                        con.close()

            # Menampilkan daftar buku yang dipinjam
            root = Tk()
            root.title("Daftar Buku yang Dipinjam")

            # Membuat Treeview untuk menampilkan daftar buku
            # Sesuaikan kolom dengan struktur tabel Anda
            tree = Treeview(root, columns=(
                "ID", "Judul", "Pengarang", 'Tanggal Pengembalian'))
            # Membuat scroll untuk Treeview
            tree_scroll = Scrollbar(
                root, orient="vertical", command=tree.yview)
            tree.configure(yscrollcommand=tree_scroll.set)
            tree_scroll.pack(side='right', fill='y')

            tree.pack(side='left', expand=True, fill='both')

            frame = Frame(root, width=200)
            frame.pack(side='left', fill='y')

            tree.heading('#0', text='No.')
            tree.column("#0", width=50, stretch=NO)

            tree.heading('#1', text='ID')
            tree.column("#1", minwidth=150, width=150, stretch=YES)

            tree.heading('#3', text='Judul')
            tree.column("#3", minwidth=150, width=150, stretch=YES)

            tree.heading('#4', text='Pengarang')
            tree.column("#4", minwidth=150, width=150, stretch=YES)

            tree.heading('#2', text='Tanggal Pengembalian')
            tree.column("#2", minwidth=150, width=150, stretch=YES)

            add_book_button = Button(
                frame, text="Kembalikan Buku", command=lambda: return_book1(tree), width=15, height=2)
            add_book_button.place(relx=0.8, rely=0.25, anchor="ne")

            # Memasukkan data buku yang dipinjam ke dalam Treeview
            for index, book in enumerate(borrowed_books, start=1):
                tree.insert("", 'end', text=index, values=book)

            tree.pack(expand=True, fill='both')
            root.mainloop()

        except pymysql.Error as error:
            print("Error terjadi:", error)

    @staticmethod
    def delete_book(tree):
        selected = tree.focus()  # Mendapatkan item yang dipilih di Treeview
        if selected:
            # Mendapatkan ID buku dari item yang dipilih
            book_id = tree.item(selected)['values'][0]
            confirm = messagebox.askyesno(
                "Hapus Buku", "Apakah Anda yakin ingin menghapus buku ini?")
            if confirm:
                try:
                    try:
                        con = mysql.connector.connect(
                            host='localhost', user='root', password='ROOT', database='admin_logindata')
                        mycursor = con.cursor()

                        query = "DELETE FROM list_books WHERE id_book = %s"
                        mycursor.execute(query, (book_id,))

                        con.commit()
                        con.close()
                        print("Buku berhasil dihapus dari database.")
                    except mysql.connector.Error as e:
                        print(f"Error: {e}")
                        print("Gagal menghapus buku dari database.")
                    messagebox.showinfo(
                        "Info", "Buku berhasil dihapus dari database.")
                    # Perbarui tampilan Treeview dengan data yang diperbarui dari database
                    # Bersihkan isi Treeview sebelum diperbarui
                    tree.delete(*tree.get_children())
                    # Populate ulang Treeview dengan data yang diperbarui dari database
                    Book.details(tree)
                except Exception as e:
                    print(f"Error: {e}")
                    messagebox.showerror(
                        "Error", "Terjadi kesalahan saat menghapus buku dari database.")

    @staticmethod
    def add_book(tree):
        def add_book_to_db():
            id = id_entry.get()
            judul = judul_entry.get()
            namapengarang = pengarang_entry.get()
            genre = genre_entry.get()
            tahunterbit = tahun_entry.get()
            ketersediaan = ketersediaan_entry.get()

            try:
                con = mysql.connector.connect(
                    host='localhost', user='root', password='ROOT', database='admin_logindata')
                mycursor = con.cursor()

                query = "INSERT INTO list_books (id_book, judul, namapengarang, genre, tahunterbit, ketersediaan) VALUES (%s, %s, %s, %s, %s, %s)"
                book_data = (id, judul, namapengarang, genre,
                             tahunterbit, ketersediaan)
                mycursor.execute(query, book_data)

                con.commit()
                con.close()
                print("Buku berhasil ditambahkan ke dalam database.")
            except mysql.connector.Error as e:
                print(f"Error: {e}")
                print("Gagal menambahkan buku ke dalam database.")
            # Memperbarui daftar buku yang ditampilkan di GUI
            Book.details(tree)

        add_window = Toplevel()
        add_window.title("Tambah Buku")
        add_window.geometry("400x300")

        id_label = Label(add_window, text="ID Buku:")
        id_label.pack()
        id_entry = Entry(add_window)
        id_entry.pack()

        judul_label = Label(add_window, text="Judul Buku:")
        judul_label.pack()
        judul_entry = Entry(add_window)
        judul_entry.pack()

        pengarang_label = Label(add_window, text="Pengarang:")
        pengarang_label.pack()
        pengarang_entry = Entry(add_window)
        pengarang_entry.pack()

        genre_label = Label(add_window, text="Genre:")
        genre_label.pack()
        genre_entry = Entry(add_window)
        genre_entry.pack()

        tahun_label = Label(add_window, text="Tahun Terbit:")
        tahun_label.pack()
        tahun_entry = Entry(add_window)
        tahun_entry.pack()

        ketersediaan_label = Label(add_window, text="Ketersediaan:")
        ketersediaan_label.pack()
        ketersediaan_entry = Entry(add_window)
        ketersediaan_entry.pack()

        submit_button = Button(
            add_window, text="Tambahkan Buku", command=add_book_to_db)
        submit_button.pack()


class Loan:
    def __init__(self):
        self.con = pymysql.connect(
            host='localhost',
            user='root', password='ROOT', database='admin_logindata')
        self.cursor = self.con.cursor()

    def __del__(self):
        if self.con:
            self.con.close()

    def calculate_penalty(self):
        try:
            query = 'SELECT id_loan, tanggal_pengembalian FROM loan_book;'
            self.cursor.execute(query)
            data_peminjaman = self.cursor.fetchall()

            tanggal_sekarang = date.today()

            for peminjaman in data_peminjaman:
                id_peminjaman = peminjaman[0]
                tanggal_pengembalian = peminjaman[1]

                if tanggal_sekarang > tanggal_pengembalian:
                    selisih_hari = (tanggal_sekarang -
                                    tanggal_pengembalian).days
                    denda = selisih_hari * 2000

                    query = f"UPDATE loan_book SET denda = {denda} WHERE id_loan = {id_peminjaman};"
                    self.cursor.execute(query)
                    self.con.commit()

        except pymysql.Error as e:
            print(f"Error: {e}")

    def get_user_info(self, username, password):
        try:
            query = 'use admin_logindata;'
            self.cursor.execute(query)
            query = 'select nim from member_logindata where username=%s and password=%s;'
            self.cursor.execute(query, (username, password))
            user_data = self.cursor.fetchone()

            id_create = ""
            while len(id_create) < 11:
                id_create += str(random.randint(1, 9))

            if user_data:
                nim_pengguna = user_data[0]
                user_info = {
                    'nim': nim_pengguna,
                    'id_loan': id_create
                }
                return user_info

        except pymysql.Error as error:
            print("Error while connecting to MySQL", error)

    def add_book_to_loan(self, tree):
        selected_items = tree.selection()
        id_book = None

        try:
            for item in selected_items:
                id_book = tree.item(item)['values'][0]

            return id_book

        except IndexError as e:
            print("Error:", e)

    def tanggal_peminjaman(self, tree, username, password):
        informasi_buku = self.add_book_to_loan(tree)
        informasi_pengguna = self.get_user_info(username, password)

        if informasi_pengguna:
            tanggal_peminjaman = date.today()
            durasi_pengurangan = timedelta(days=7)
            tanggal_pengembalian = tanggal_peminjaman + durasi_pengurangan

            try:
                sql = "INSERT INTO loan_book (id_book, id_loan, nim, tanggal_peminjaman, tanggal_pengembalian) VALUES (%s, %s, %s, %s, %s)"
                self.cursor.execute(
                    sql, (informasi_buku, informasi_pengguna['id_loan'], informasi_pengguna['nim'], tanggal_peminjaman, tanggal_pengembalian))
                self.con.commit()
                print("Data berhasil ditambahkan ke database")

            except pymysql.Error as e:
                print(f"Terjadi kesalahan: {e}")


def adminlogin():

    def Date_Tim():
        time_string = time.strftime("%H:%M:%S")
        date_string = time.strftime("%d/%m/%Y")
        clockdateLabel.configure(text=" Date : " + date_string)
        clocktimLabel.configure(text=" Time : " + time_string)
        clocktimLabel.after(1000, Date_Tim)

    dashwin = Toplevel()
    dashwin.geometry("900x550+300+100")
    dashwin.iconbitmap('LibraryIcon.ico')
    dashwin.title("Library Management System")

    root_title = Label(dashwin, text="DASHBOARD",
                       fg="white",
                       bg='#6D93B1',
                       font=("Courier New", 40, "bold"),
                       relief='groove', bd=2)
    root_title.pack(side='top', fill='x')

    Admin_dateFrame = Frame(dashwin, bg="#E5EACA",
                            height=48, relief='groove', bd=5)
    Admin_dateFrame.pack(fill='x')

    nameLabel = Label(Admin_dateFrame, text="Name:",
                      font=("Arial", 13, "bold"), bg="#E5EACA")
    nameLabel.place(x=10, y=0, relheight=1)

    nameLabel = Label(Admin_dateFrame, text="Name:",
                      font=("Arial", 13, "bold"), bg="#E5EACA")
    nameLabel.place(x=10, y=0, relheight=1)

# Membuat instance dari ProfilePage
    profile_page = ProfilePage(master=root)
    profile_page.pack()

    # Fungsi untuk menampilkan profil saat event terjadi
    def show_profile(event):
        profile_page.show_profile()

    # nama user
    nameValLabel = Label(Admin_dateFrame, text=Admin_name, font=(
        "Arial", 14, "italic bold"), fg='red', bg="#E5EACA", padx=5)
    nameValLabel.place(x=68, y=0, relheight=1)
    nameValLabel.bind("<Button-1>", show_profile)

    clockdateLabel = Label(Admin_dateFrame, image=calanderimg, font=(
        'times', 14, 'bold'), relief='flat', bg='#E5EACA', compound='left')
    clockdateLabel.place(x=470, y=0, relheight=1)

    clocktimLabel = Label(Admin_dateFrame, image=clockimg, font=(
        'times', 14, 'bold'), relief='flat', bg='#E5EACA', compound='left')
    clocktimLabel.place(x=690, y=0, relheight=1)
    Date_Tim()

    frame = Frame(dashwin)
    frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

    tree = Treeview(frame, columns=("id", "judul", "namapengarang", "genre",
                    "tahunterbit", "ketersediaan"), selectmode="extended", height=15)
    tree.pack(side=LEFT, fill=Y)

    vsb = Scrollbar(frame, orient="vertical", command=tree.yview)
    vsb.pack(side=RIGHT, fill=Y)
    tree.configure(yscrollcommand=vsb.set)

    tree.column("#0", width=0, stretch=NO)
    tree.heading("#0", text="", anchor=CENTER)

    tree.heading("#1", text="ID")
    tree.column("#1", minwidth=50, width=50, stretch=YES)

    tree.heading("#2", text="Title")
    tree.column("#2", minwidth=150, width=150, stretch=YES)

    tree.heading("#3", text="Author")
    tree.column("#3", minwidth=150, width=150, stretch=YES)

    tree.heading("#4", text="Genre")
    tree.column("#4", minwidth=150, width=150, stretch=YES)

    tree.heading("#5", text="Publication Year")
    tree.column("#5", minwidth=100, width=100, stretch=YES)

    tree.heading("#6", text="Availability")
    tree.column("#6", minwidth=100, width=100, stretch=YES)

    Book.details(tree)  # Populate the Treeview with books

    # Tombol "Pinjam"
    pinjam_button = Button(frame, text="Pinjam", command=lambda: Book.pinjam_book(
        tree), width=15, height=2)
    pinjam_button.place(relx=0.95, rely=0.05, anchor="ne")
    # Tombol "Kembalikan"
    pinjam_button = Button(frame, text="Kembalikan",
                           command=lambda: Book.return_book(tree), width=15, height=2)
    pinjam_button.place(relx=0.95, rely=0.15, anchor="ne")

    # Tombol untuk menambahkan buku
    add_book_button = Button(frame, text="Tambah Buku",
                             command=lambda: Book.add_book(tree), width=15, height=2)
    add_book_button.place(relx=0.95, rely=0.25, anchor="ne")

    # Tombol Hapus Buku
    delete_book_button = Button(
        frame, text="Hapus Buku", command=lambda: Book.delete_book(tree), width=15, height=2)
    delete_book_button.place(relx=0.95, rely=0.35, anchor="ne")


root.mainloop()
