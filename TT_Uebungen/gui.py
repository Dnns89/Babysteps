import tkinter as tk
from tkinter import ttk, messagebox
import storage
import logic
from models import all_categories, exercises
from datetime import datetime


class TrainingAppGUI:
    def __init__(self, root):
        self.root = root
        self.last_plan = None
        self.last_total_duration = 0

        # Notebook / Tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Tabs initialisieren
        self.setup_planer_tab()
        self.setup_stats_tab()

    def setup_planer_tab(self):
        self.tab_planer = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_planer, text="📅 Trainingsplaner")

        self.tab_planer.columnconfigure(0, minsize=200)
        self.tab_planer.columnconfigure(1, weight=1)

        # --- Sidebar ---
        sidebar = ttk.Frame(self.tab_planer)
        sidebar.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)

        ttk.Label(sidebar, text="Kategorien auswählen:", font=("Segoe UI", 10, "bold")).pack(anchor="w")
        self.category_vars = {}
        for cat in all_categories:
            var = tk.BooleanVar()
            ttk.Checkbutton(sidebar, text=cat, variable=var).pack(anchor="w")
            self.category_vars[cat] = var

        ttk.Separator(sidebar, orient="horizontal").pack(fill="x", pady=10)

        # Schwierigkeit
        ttk.Label(sidebar, text="Schwierigkeit:", font=("Segoe UI", 10, "bold")).pack(anchor="w")
        self.difficulty_var = tk.IntVar(value=0)
        self.diff_label_var = tk.StringVar(value="Alle Schwierigkeitsgrade")

        scale = ttk.Scale(sidebar, from_=0, to=5, orient="horizontal",
                          variable=self.difficulty_var, command=self.update_diff_label)
        scale.pack(fill="x", padx=5)
        ttk.Label(sidebar, textvariable=self.diff_label_var).pack(anchor="w")

        # Modus
        ttk.Label(sidebar, text="Modus:", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(10, 0))
        self.mode_var = tk.StringVar(value="anzahl")
        ttk.Radiobutton(sidebar, text="Anzahl Übungen", variable=self.mode_var,
                        value="anzahl", command=self.toggle_mode_widgets).pack(anchor="w")
        ttk.Radiobutton(sidebar, text="Gesamtzeit", variable=self.mode_var,
                        value="zeit", command=self.toggle_mode_widgets).pack(anchor="w")

        self.num_ex_var = tk.StringVar(value="3")
        self.num_menu = ttk.Combobox(sidebar, textvariable=self.num_ex_var,
                                     values=[str(i) for i in range(1, 11)], state="readonly")
        self.num_menu.pack(fill="x", pady=2)

        self.time_var = tk.IntVar(value=30)
        self.time_menu = ttk.Combobox(sidebar, textvariable=self.time_var,
                                      values=[10, 20, 30, 40, 50, 60], state="disabled")
        self.time_menu.pack(fill="x", pady=2)

        # Buttons
        ttk.Button(sidebar, text="Plan erstellen", command=self.on_generate).pack(fill="x", pady=(10, 2))
        ttk.Button(sidebar, text="Zufälliger Plan", command=self.on_random).pack(fill="x", pady=2)
        ttk.Button(sidebar, text="✅ Plan absolvieren", command=self.on_confirm).pack(fill="x", pady=10)

        # --- Main Area (Text Output) ---
        main_area = ttk.Frame(self.tab_planer)
        main_area.grid(row=0, column=1, sticky="nswe", padx=5, pady=5)

        self.output_text = tk.Text(main_area, wrap="word", font=("Segoe UI", 10))
        self.output_text.pack(fill="both", expand=True)
        self.output_text.tag_configure("bold", font=("Segoe UI", 10, "bold"))

    def setup_stats_tab(self):
        self.tab_stats = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_stats, text="📊 Statistiken")

        container = ttk.Frame(self.tab_stats, padding=20)
        container.pack(fill="both", expand=True)

        # Header
        header = ttk.Frame(container)
        header.pack(fill="x")
        ttk.Label(header, text="📊 Deine Fortschritte", font=("Segoe UI", 12, "bold")).pack(side="left")
        ttk.Button(header, text="👤 Name ändern", command=self.on_change_name).pack(side="right", padx=2)

        # Stats Labels
        self.stat_vars = {
            "name": tk.StringVar(), "plans": tk.StringVar(),
            "ex": tk.StringVar(), "min": tk.StringVar()
        }
        for key in self.stat_vars:
            ttk.Label(container, textvariable=self.stat_vars[key]).pack(anchor="w", pady=2)

        # Treeview
        self.tree = ttk.Treeview(container, columns=("Kat", "Anz"), show="headings", height=8)
        self.tree.heading("Kat", text="Kategorie")
        self.tree.heading("Anz", text="Anzahl")
        self.tree.pack(fill="x", pady=10)

        # Ziele Bereich
        ttk.Label(container, text="🎯 Wochenziele", font=("Segoe UI", 10, "bold")).pack(anchor="w")
        self.goal_min_var = tk.IntVar()
        self.goal_ex_var = tk.IntVar()

        f_goals = ttk.Frame(container)
        f_goals.pack(fill="x")
        ttk.Label(f_goals, text="Minuten:").grid(row=0, column=0)
        ttk.Entry(f_goals, textvariable=self.goal_min_var, width=8).grid(row=0, column=1, padx=5)
        ttk.Label(f_goals, text="Übungen:").grid(row=0, column=2)
        ttk.Entry(f_goals, textvariable=self.goal_ex_var, width=8).grid(row=0, column=3, padx=5)
        ttk.Button(f_goals, text="Speichern", command=self.on_save_goals).grid(row=0, column=4, padx=10)

        self.goal_status_var = tk.StringVar(value="Keine Ziele gesetzt")
        ttk.Label(container, textvariable=self.goal_status_var, foreground="green").pack(anchor="w", pady=5)

    # --- Logik-Anbindung (Callbacks) ---
    def update_diff_label(self, val):
        v = int(float(val))
        self.diff_label_var.set("Alle" if v == 0 else f"bis {v}/5")

    def toggle_mode_widgets(self):
        if self.mode_var.get() == "anzahl":
            self.num_menu.configure(state="readonly")
            self.time_menu.configure(state="disabled")
        else:
            self.num_menu.configure(state="disabled")
            self.time_menu.configure(state="readonly")

    def on_generate(self):
        cats = [c for c, v in self.category_vars.items() if v.get()]
        if not cats:
            messagebox.showwarning("Auswahl", "Bitte Kategorien wählen")
            return

        pool = logic.get_exercises_by_categories(cats, self.difficulty_var.get())
        self.process_plan_creation(pool)

    def on_random(self):
        self.process_plan_creation(exercises)

    def process_plan_creation(self, pool):
        if not pool:
            messagebox.showinfo("Leer", "Keine Übungen gefunden")
            return

        if self.mode_var.get() == "anzahl":
            plan, dur = logic.generate_plan_by_count(pool, int(self.num_ex_var.get()))
        else:
            plan, dur = logic.generate_plan_by_time(pool, self.time_var.get())

        self.last_plan = plan
        self.last_total_duration = dur
        self.display_plan(plan, dur)

    def display_plan(self, plan, duration):
        self.output_text.delete(1.0, tk.END)
        for i, ex in enumerate(plan, 1):
            self.output_text.insert(tk.END, f"{i}. {ex.name} ({ex.duration} min p.P.)\n", "bold")
            self.output_text.insert(tk.END, f"   {ex.description}\n\n")
        self.output_text.insert(tk.END, f"🕒 Gesamtdauer: {duration} Minuten", "bold")

    def on_confirm(self):
        if not self.last_plan:
            return
        if messagebox.askyesno("Bestätigung", "Plan absolviert?"):
            storage.update_stats(self.last_plan, self.last_total_duration)
            self.refresh_all()
            messagebox.showinfo("Super!", "Training gespeichert")

    def on_save_goals(self):
        storage.user["ziele"]["woechentlich_minuten"] = self.goal_min_var.get()
        storage.user["ziele"]["woechentlich_uebungen"] = self.goal_ex_var.get()
        storage.save_user()
        self.refresh_all()

    def on_change_name(self):
        storage.ask_new_user(self.root)
        self.refresh_all()

    def refresh_all(self):
        u = storage.user
        s = u["stats"]
        self.stat_vars["name"].set(f"👤 Spieler: {u['name']}")
        self.stat_vars["plans"].set(f"🗂️ Pläne: {s['plaene_erstellt']}")
        self.stat_vars["ex"].set(f"🏓 Übungen: {s['uebungen_absolviert']}")
        self.stat_vars["min"].set(f"🕒 Zeit: {s['gesamtzeit']} Min")

        # Treeview
        for row in self.tree.get_children(): self.tree.delete(row)
        for cat, count in sorted(s["kategorien"].items(), key=lambda x: -x[1]):
            self.tree.insert("", tk.END, values=(cat, count))

        # Ziele Anzeige
        self.goal_min_var.set(u["ziele"].get("woechentlich_minuten", 0))
        self.goal_ex_var.set(u["ziele"].get("woechentlich_uebungen", 0))

        # --- Ziel-Check Status ---
        msg = []

        # 1. Minuten-Ziel prüfen
        goal_min = u["ziele"].get("woechentlich_minuten", 0)
        if goal_min > 0:
            status_min = "✅" if s["gesamtzeit"] >= goal_min else "❌"
            msg.append(f"{status_min} Minuten-Ziel ({s['gesamtzeit']}/{goal_min})")

        # 2. Übungen-Ziel prüfen (Das hat wahrscheinlich gefehlt!)
        goal_ex = u["ziele"].get("woechentlich_uebungen", 0)
        if goal_ex > 0:
            status_ex = "✅" if s["uebungen_absolviert"] >= goal_ex else "❌"
            msg.append(f"{status_ex} Übungen-Ziel ({s['uebungen_absolviert']}/{goal_ex})")

        # Anzeige aktualisieren
        if msg:
            self.goal_status_var.set("\n".join(msg))
        else:
            self.goal_status_var.set("Keine Ziele gesetzt")