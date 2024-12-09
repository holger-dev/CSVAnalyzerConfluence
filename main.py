import tkinter as tk
from tkinter import filedialog, messagebox
import csv

class CSVAnalyzerApp:
    def __init__(self, master):
        self.master = master
        master.title("CSV Analyzer")
        master.geometry("1400x600")  # Fenstergröße auf 1400 Pixel Breite erhöhen

        # Button zum Importieren der CSV-Datei
        self.import_button = tk.Button(master, text="CSV Datei importieren", command=self.load_csv)
        self.import_button.pack(pady=10)

        # Frame für Gruppen
        self.group_frame = tk.Frame(master)
        self.group_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Überschrift für Gruppen
        self.group_count_label = tk.Label(self.group_frame, text="Gruppen: 0", font=("Helvetica", 12))
        self.group_count_label.pack(pady=5)
        tk.Label(self.group_frame, text="Gruppen", font=("Helvetica", 16)).pack(pady=5)

        # Suchleiste für Gruppen
        self.group_search_var = tk.StringVar()
        self.group_search_entry = tk.Entry(self.group_frame, textvariable=self.group_search_var)
        self.group_search_entry.pack(pady=5, fill=tk.X, expand=True)
        tk.Label(self.group_frame, text="Suche nach Gruppen:").pack()

        # Listen für Gruppen
        self.group_listbox = tk.Listbox(self.group_frame, width=40, height=25)
        self.group_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar für Gruppen
        self.group_scrollbar = tk.Scrollbar(self.group_frame)
        self.group_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.group_listbox.config(yscrollcommand=self.group_scrollbar.set)
        self.group_scrollbar.config(command=self.group_listbox.yview)

        # Frame für Benutzer
        self.user_frame = tk.Frame(master)
        self.user_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Überschrift für Benutzer
        self.user_count_label = tk.Label(self.user_frame, text="Benutzer: 0", font=("Helvetica", 12))
        self.user_count_label.pack(pady=5)
        tk.Label(self.user_frame, text="Benutzer", font=("Helvetica", 16)).pack(pady=5)

        # Suchleiste für Benutzer
        self.user_search_var = tk.StringVar()
        self.user_search_entry = tk.Entry(self.user_frame, textvariable=self.user_search_var)
        self.user_search_entry.pack(pady=5, fill=tk.X, expand=True)
        tk.Label(self.user_frame, text="Suche nach Benutzern:").pack()

        # Listen für Personen
        self.person_listbox = tk.Listbox(self.user_frame, width=40, height=25)
        self.person_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar für Benutzer
        self.user_scrollbar = tk.Scrollbar(self.user_frame)
        self.user_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.person_listbox.config(yscrollcommand=self.user_scrollbar.set)
        self.user_scrollbar.config(command=self.person_listbox.yview)

        # Buttons für die Analyse
        self.is_in_group_button = tk.Button(master, text="In Gruppe", command=self.show_users_in_group)
        self.is_in_group_button.pack(pady=5)

        self.is_not_in_group_button = tk.Button(master, text="Nicht in Gruppe", command=self.show_users_not_in_group)
        self.is_not_in_group_button.pack(pady=5)

        self.reset_filter_button = tk.Button(master, text="Filter zurücksetzen", command=self.reset_filters)
        self.reset_filter_button.pack(pady=5)

        # Anleitung als Label
        self.instruction_label = tk.Label(master, text="Anleitung:\n"
                                                        "1. Importiere eine CSV-Datei mit Gruppen und Benutzern.\n"
                                                        "2. Suche nach Gruppen oder Benutzern mit den Suchfeldern.\n"
                                                        "3. Wähle eine Gruppe oder einen Benutzer aus\nund klicke auf die entsprechenden Buttons,"
                                                        " um die Informationen anzuzeigen.\n"
                                                        "4. Klicke auf 'Filter zurücksetzen', um die Suchfelder zu leeren.",
                                            wraplength=900, justify="left")
        self.instruction_label.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        self.group_data = {}  # Speichert die Zuordnung von Benutzern zu Gruppen

        # Bindings für die Suchfunktion
        self.group_search_entry.bind("<KeyRelease>", self.filter_groups)
        self.user_search_entry.bind("<KeyRelease>", self.filter_users)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                self.group_data = {}
                result_all_users = set()
                result_groups = set()

                with open(file_path, newline='') as csv_file:
                    all_rows = csv.DictReader(csv_file, delimiter=',', quotechar='"')
                    for row in all_rows:
                        group_name = row['Group name']
                        user_name = row['User name']

                        # Alle Gruppen und Benutzer sammeln
                        result_groups.add(group_name)
                        result_all_users.add(user_name)

                        # Benutzer in Gruppen speichern
                        if group_name not in self.group_data:
                            self.group_data[group_name] = set()
                        self.group_data[group_name].add(user_name)

                # Listboxen aktualisieren
                self.update_group_listbox(sorted(result_groups))
                self.update_person_listbox(sorted(result_all_users))

            except Exception as e:
                messagebox.showerror("Fehler", f"Fehler beim Laden der CSV-Datei: {e}")

    def update_group_listbox(self, groups):
        self.group_listbox.delete(0, tk.END)
        for group in groups:
            self.group_listbox.insert(tk.END, group)
        self.group_count_label.config(text=f"Gruppen: {len(groups)}")  # Aktualisierung der Gruppenanzahl

    def update_person_listbox(self, users):
        self.person_listbox.delete(0, tk.END)
        for user in users:
            self.person_listbox.insert(tk.END, user)
        self.user_count_label.config(text=f"Benutzer: {len(users)}")  # Aktualisierung der Benutzeranzahl

    def filter_groups(self, event):
        search_term = self.group_search_var.get().lower()
        filtered_groups = [group for group in self.group_data.keys() if search_term in group.lower()]
        self.update_group_listbox(sorted(filtered_groups))

    def filter_users(self, event):
        search_term = self.user_search_var.get().lower()
        filtered_users = [user for user in set(user for users in self.group_data.values() for user in users) if search_term in user.lower()]
        self.update_person_listbox(sorted(filtered_users))

    def show_users_in_group(self):
        selected_group = self.group_listbox.curselection()
        selected_person = self.person_listbox.curselection()

        if selected_group:
            group = self.group_listbox.get(selected_group)
            users_in_group = sorted(self.group_data.get(group, []))
            self.update_person_listbox(users_in_group)
        elif selected_person:
            person = self.person_listbox.get(selected_person)
            groups_of_user = sorted([group for group, users in self.group_data.items() if person in users])
            self.update_group_listbox(groups_of_user)  # Zeige die Gruppen in der Gruppen-Listbox an
        else:
            messagebox.showwarning("Auswahl erforderlich", "Bitte wählen Sie eine Gruppe oder einen Benutzer aus.")

    def show_users_not_in_group(self):
        selected_group = self.group_listbox.curselection()
        selected_person = self.person_listbox.curselection()

        if selected_group:
            group = self.group_listbox.get(selected_group)
            all_users = set(user for users in self.group_data.values() for user in users)
            users_in_group = self.group_data.get(group, set())
            users_not_in_group = sorted(all_users - users_in_group)
            self.update_person_listbox(users_not_in_group)
        elif selected_person:
            person = self.person_listbox.get(selected_person)
            groups_of_user = sorted([group for group, users in self.group_data.items() if person in users])
            all_groups = sorted(self.group_data.keys())
            groups_not_of_user = sorted(set(all_groups) - set(groups_of_user))
            self.update_group_listbox(groups_not_of_user)  # Zeige die Gruppen nicht in der Gruppen-Listbox an
        else:
            messagebox.showwarning("Auswahl erforderlich", "Bitte wählen Sie eine Gruppe oder einen Benutzer aus.")

    def reset_filters(self):
        # Zurücksetzen der Suchfelder und Listboxen
        self.group_search_var.set("")
        self.user_search_var.set("")
        self.update_group_listbox(sorted(self.group_data.keys()))
        self.update_person_listbox(sorted(set(user for users in self.group_data.values() for user in users)))

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVAnalyzerApp(root)
    root.mainloop()