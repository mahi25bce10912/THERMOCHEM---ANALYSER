import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

# ------------------ Main App ------------------
class ThermoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ThermoChem Analyzer Pro")
        self.root.geometry("900x620")
        self.root.configure(bg="#141824")
        self.root.resizable(False, False)

        self.result_var = tk.StringVar()

        self.create_header()
        self.create_sidebar()
        self.create_main_area()

    # ---------- Header ----------
    def create_header(self):
        tk.Label(
            self.root,
            text="ThermoChem Analyzer",
            font=("Helvetica", 20, "bold"),
            bg="#141824",
            fg="#ffffff"
        ).pack(pady=12)

    # ---------- Sidebar ----------
    def create_sidebar(self):
        self.sidebar = tk.Frame(self.root, bg="#1f2638", width=200)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        buttons = [
            ("Calorimetry", self.show_calorimetry),
            ("Gibbs Energy", self.show_gibbs),
            ("Enthalpy", self.show_enthalpy),
            ("Phase Change", self.show_phase),
            ("Heat Engine", self.show_engine),
            ("Entropy Graph", self.show_entropy),
            ("Molecular Shape", self.show_structure),
            ("Bond Polarity", self.show_polarity)
        ]

        tk.Label(
            self.sidebar,
            text="Modules",
            font=("Helvetica", 14, "bold"),
            bg="#1f2638",
            fg="white"
        ).pack(pady=14)

        for text, command in buttons:
            tk.Button(
                self.sidebar,
                text=text,
                command=command,
                width=20,
                bg="#2f3b55",
                fg="white",
                activebackground="#4a5d85",
                relief="flat",
                font=("Arial", 10, "bold"),
                pady=6,
                cursor="hand2"
            ).pack(pady=5)

    # ---------- Main Area ----------
    def create_main_area(self):
        self.main = tk.Frame(self.root, bg="#eef2f7")
        self.main.pack(side="right", expand=True, fill="both")

        self.result_label = tk.Label(
            self.main,
            textvariable=self.result_var,
            font=("Arial", 13, "bold"),
            bg="#dfe7f2",
            fg="#0b2e59",
            justify="left",
            padx=20,
            pady=10,
            relief="groove"
        )
        self.result_label.pack(side="bottom", pady=15)

    def clear_main(self):
        for widget in self.main.winfo_children():
            if widget != self.result_label:
                widget.destroy()

    # ---------- Helper ----------
    def labeled_entry(self, parent, label_text, default_val):
        frame = tk.Frame(parent, bg="#eef2f7")
        frame.pack(pady=5)

        tk.Label(
            frame,
            text=label_text,
            width=34,
            anchor='w',
            bg="#eef2f7",
            font=("Arial", 10, "bold")
        ).pack(side="left")

        entry = tk.Entry(
            frame,
            width=18,
            font=("Arial", 10),
            bd=2,
            relief="groove"
        )
        entry.pack(side="left")
        entry.insert(0, default_val)
        return entry

    # ---------- Calorimetry ----------
    def show_calorimetry(self):
        self.clear_main()
        tk.Label(self.main, text="Calorimetry (q = mcΔT)", font=("Helvetica", 15, "bold"), bg="#eef2f7").pack(pady=15)

        self.mass = self.labeled_entry(self.main, "Mass of substance (g):", "100")
        self.c = self.labeled_entry(self.main, "Specific heat capacity (J/g°C):", "4.18")
        self.dt = self.labeled_entry(self.main, "Temperature change ΔT (°C):", "25")
        self.initial_temp = self.labeled_entry(self.main, "Initial temperature (°C):", "20")

        tk.Button(self.main, text="Calculate Heat", command=self.calc_heat, bg="#2f7ed8", fg="white").pack(pady=15)

    def calc_heat(self):
        try:
            q = float(self.mass.get()) * float(self.c.get()) * float(self.dt.get())
            final_temp = float(self.initial_temp.get()) + float(self.dt.get())
            self.result_var.set(f"Heat Energy = {q:.2f} J\nFinal Temperature = {final_temp:.2f} °C")
        except:
            messagebox.showerror("Error", "Invalid Input")

    # ---------- Gibbs ----------
    def show_gibbs(self):
        self.clear_main()
        tk.Label(self.main, text="Gibbs Free Energy", font=("Helvetica", 15, "bold"), bg="#eef2f7").pack(pady=15)

        self.h = self.labeled_entry(self.main, "Enthalpy change ΔH (J):", "-50000")
        self.s = self.labeled_entry(self.main, "Entropy change ΔS (J/K):", "-120")
        self.t = self.labeled_entry(self.main, "Temperature T (K):", "298")
        self.pressure = self.labeled_entry(self.main, "System pressure (atm):", "1")

        tk.Button(self.main, text="Calculate ΔG", command=self.calc_gibbs, bg="#2f7ed8", fg="white").pack(pady=5)
        tk.Button(self.main, text="Plot ΔG Graph", command=self.plot_gibbs, bg="#4a5d85", fg="white").pack(pady=5)

    def calc_gibbs(self):
        try:
            g = float(self.h.get()) - float(self.t.get()) * float(self.s.get())
            state = "Spontaneous" if g < 0 else "Non-Spontaneous"
            self.result_var.set(f"ΔG = {g:.2f} J → {state}\nPressure = {self.pressure.get()} atm")
        except:
            messagebox.showerror("Error", "Invalid Input")

    def plot_gibbs(self):
        try:
            T = np.linspace(1, 600, 100)
            G = float(self.h.get()) - T * float(self.s.get())
            plt.figure()
            plt.plot(T, G)
            plt.xlabel("Temperature (K)")
            plt.ylabel("ΔG (J)")
            plt.title("Gibbs Free Energy vs Temperature")
            plt.grid(True)
            plt.show()
        except:
            messagebox.showerror("Error", "Invalid Input")

    # ---------- Enthalpy ----------
    def show_enthalpy(self):
        self.clear_main()
        tk.Label(self.main, text="Enthalpy (Hess Law)", font=("Helvetica", 15, "bold"), bg="#eef2f7").pack(pady=15)
        self.react = self.labeled_entry(self.main, "Reactants enthalpy (kJ/mol):", "-250")
        self.prod = self.labeled_entry(self.main, "Products enthalpy (kJ/mol):", "-400")
        self.moles = self.labeled_entry(self.main, "Number of moles:", "2")
        tk.Button(self.main, text="Calculate ΔH", command=self.calc_h, bg="#2f7ed8", fg="white").pack(pady=15)

    def calc_h(self):
        try:
            dh = float(self.prod.get()) - float(self.react.get())
            total = dh * float(self.moles.get())
            self.result_var.set(f"ΔH = {dh:.2f} kJ/mol\nTotal Enthalpy = {total:.2f} kJ")
        except:
            messagebox.showerror("Error", "Invalid Input")

    # ---------- Phase ----------
    def show_phase(self):
        self.clear_main()
        tk.Label(self.main, text="Phase Change Energy", font=("Helvetica", 15, "bold"), bg="#eef2f7").pack(pady=15)
        self.mass2 = self.labeled_entry(self.main, "Mass undergoing phase change (g):", "50")
        self.lh = self.labeled_entry(self.main, "Latent heat (J/g):", "334")
        self.phase_type = self.labeled_entry(self.main, "Phase process:", "melting")
        tk.Button(self.main, text="Calculate Energy", command=self.calc_phase, bg="#2f7ed8", fg="white").pack(pady=15)

    def calc_phase(self):
        try:
            q = float(self.mass2.get()) * float(self.lh.get())
            self.result_var.set(f"Phase Change Energy = {q:.2f} J\nProcess = {self.phase_type.get()}")
        except:
            messagebox.showerror("Error", "Invalid Input")

    # ---------- Heat Engine ----------
    def show_engine(self):
        self.clear_main()
        tk.Label(self.main, text="Heat Engine Efficiency", font=("Helvetica", 15, "bold"), bg="#eef2f7").pack(pady=15)
        self.th = self.labeled_entry(self.main, "Hot reservoir temperature (K):", "500")
        self.tc = self.labeled_entry(self.main, "Cold reservoir temperature (K):", "300")
        self.work_output = self.labeled_entry(self.main, "Work output (J):", "1000")
        tk.Button(self.main, text="Calculate Efficiency", command=self.calc_eff, bg="#2f7ed8", fg="white").pack(pady=15)

    def calc_eff(self):
        try:
            eff = 1 - float(self.tc.get()) / float(self.th.get())
            self.result_var.set(f"Carnot Efficiency = {eff*100:.2f}%\nWork Output = {self.work_output.get()} J")
        except:
            messagebox.showerror("Error", "Invalid Input")

    # ---------- Entropy ----------
    def show_entropy(self):
        self.clear_main()
        tk.Label(self.main, text="Entropy Trend", font=("Helvetica", 15, "bold"), bg="#eef2f7").pack(pady=15)
        tk.Button(self.main, text="Plot Entropy Graph", command=self.plot_entropy, bg="#4a5d85", fg="white").pack(pady=20)

    def plot_entropy(self):
        states = ['Solid', 'Liquid', 'Gas']
        values = [1, 5, 10]
        plt.figure()
        plt.plot(states, values, marker='o')
        plt.title("Entropy Trend")
        plt.xlabel("State")
        plt.ylabel("Relative Entropy")
        plt.grid(True)
        plt.show()

    # ---------- Molecular Shape ----------
    def show_structure(self):
        self.clear_main()
        tk.Label(self.main, text="Molecular Shape Predictor", font=("Helvetica", 15, "bold"), bg="#eef2f7").pack(pady=15)
        self.electron_pairs = self.labeled_entry(self.main, "Number of electron pairs:", "4")
        tk.Button(self.main, text="Predict Shape", command=self.predict_shape, bg="#2f7ed8", fg="white").pack(pady=15)

        self.shape_canvas = tk.Canvas(
            self.main,
            width=420,
            height=260,
            bg="white",
            highlightthickness=1,
            highlightbackground="gray"
        )
        self.shape_canvas.pack(pady=15)

    def predict_shape(self):
        try:
            pairs = int(self.electron_pairs.get())
            shapes = {2: "Linear", 3: "Trigonal Planar", 4: "Tetrahedral"}
            shape = shapes.get(pairs, "Complex shape")
            self.result_var.set(f"Predicted Molecular Geometry = {shape}")
            self.draw_molecule(shape)
        except:
            messagebox.showerror("Error", "Invalid Input")

    def draw_molecule(self, shape):
        canvas = self.shape_canvas
        canvas.delete("all")

        cx, cy = 210, 130
        r_center = 18
        r_outer = 14

        canvas.create_oval(cx-r_center, cy-r_center, cx+r_center, cy+r_center, fill="#2f7ed8")
        canvas.create_text(cx, cy, text="A", fill="white", font=("Arial", 11, "bold"))

        if shape == "Linear":
            positions = [(110, 130), (310, 130)]
        elif shape == "Trigonal Planar":
            positions = [(210, 50), (130, 210), (290, 210)]
        elif shape == "Tetrahedral":
            positions = [(210, 40), (110, 180), (310, 180), (210, 235)]
        else:
            positions = []

        for x, y in positions:
            canvas.create_line(cx, cy, x, y, width=3)
            canvas.create_oval(x-r_outer, y-r_outer, x+r_outer, y+r_outer, fill="#3cb371")
            canvas.create_text(x, y, text="X", fill="white", font=("Arial", 10, "bold"))

    # ---------- Bond Polarity ----------
    def show_polarity(self):
        self.clear_main()
        tk.Label(self.main, text="Bond Polarity Analyzer", font=("Helvetica", 15, "bold"), bg="#eef2f7").pack(pady=15)
        self.en1 = self.labeled_entry(self.main, "Electronegativity of atom 1:", "3.5")
        self.en2 = self.labeled_entry(self.main, "Electronegativity of atom 2:", "2.1")
        tk.Button(self.main, text="Analyze Bond", command=self.analyze_polarity, bg="#2f7ed8", fg="white").pack(pady=15)

    def analyze_polarity(self):
        try:
            diff = abs(float(self.en1.get()) - float(self.en2.get()))
            bond = "Nonpolar Covalent" if diff < 0.4 else "Polar Covalent"
            self.result_var.set(f"Electronegativity Difference = {diff:.2f}\nBond Type = {bond}")
        except:
            messagebox.showerror("Error", "Invalid Input")

# ------------------ Run App ------------------
root = tk.Tk()
app = ThermoApp(root)
root.mainloop()
