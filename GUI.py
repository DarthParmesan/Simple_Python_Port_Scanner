import tkinter as tk
import tkinter.filedialog
import datetime

from Scanner import *

GUI_SIZE = "400x400"
GUI_TITLE = "Python Port Scanner"


class GUI:

    ports = []
    elapsed = ""


    def __init__(self):
        self.output_console = None
        self.end_port = None
        self.start_port = None
        self.target_input = None
        self.root = tk.Tk()
        self.root.geometry(GUI_SIZE)
        self.root.title(GUI_TITLE)
        self.root.resizable(False, False)
        self.init_components()

        self.scanned = False

        self.scanner = Scanner()

    def run(self):
        self.root.mainloop()
        pass

    def init_components(self):

        y0 = 20

        # Labels.
        tk.Label(self.root, text="Target IP:", font=("Courier", 10)).place(x=20, y=y0)
        tk.Label(self.root, text="Ports:", font=("Courier", 10)).place(x=52, y=y0 + 25)
        tk.Label(self.root, text=">", font=("Courier", 10)).place(x=168, y=y0 + 25)
        tk.Label(self.root, text="Output Console >> ", font=("Courier", 10)).place(x=20, y=y0 + 75)

        # Input.
        self.target_input = tk.Entry(self.root, font=("Courier", 10))
        self.target_input.place(x=110, y=y0, width=130)
        self.start_port = tk.Entry(self.root, font=("Courier", 10))
        self.start_port.place(x=110, y=y0 + 25, width=55)
        self.end_port = tk.Entry(self.root, font=("Courier", 10))
        self.end_port.place(x=185, y=y0 + 25, width=55)

        # Buttons.
        tk.Button(self.root, font=("Courier", 10), text="Start Scan", width=12, command=self.start_scan).place(x=275,
                                                                                                               y=y0 + 100)
        tk.Button(self.root, font=("Courier", 10), text="Save Scan", width=12, command=self.save_scan).place(x=275,
                                                                                                             y=y0 + 135)
        tk.Button(self.root, font=("Courier", 10), text="Exit", width=12, command=self.kill).place(x=275, y=y0 + 320)

        # Output.
        self.output_console = tk.Text(self.root, font=("Courier", 10), fg="green", bg="black")
        self.output_console.place(x=20, y=y0 + 100, width=230, height=250)
        self.opening_banner()

    def start_scan(self):



        ip = self.target_input.get()
        start = self.start_port.get()
        end = self.end_port.get()

        if self.validate_input(ip, start, end):

            self.start_scan_banner(ip, start, end)
            # start scanning ports.
            self.ports, self.elapsed = self.scanner.scan(ip, start, end)

            self.print_results(self.ports, self.elapsed)
            self.scanned = True

        else:
            self.output_console.delete(1.0, "end")
            self.output_console.insert(tk.END, "\n\n")
            self.output_console.insert(tk.END, "-" * 28 + "\n")
            self.output_console.insert(tk.END, " ERROR: Please Enter a valid  IP address and port range!.\n")
            self.output_console.insert(tk.END, "-" * 28 + "\n")

    def opening_banner(self):
        # print a nice banner when the program opens?.
        self.output_console.insert(tk.END, "-" * 28 + "\n")
        self.output_console.insert(tk.END, "   -Simple Port Scanner-" + "\n\n")
        self.output_console.insert(tk.END, " djs 01/05/22\n")
        self.output_console.insert(tk.END, "-" * 28 + "\n")
        self.output_console.insert(tk.END, " Input a target IP address \n and a port range to scan.\n\n\n")

        # then print a bunny!!
        self.output_console.insert(tk.END, "         (\ /)              \n")
        self.output_console.insert(tk.END, "         ( . .)             \n")
        self.output_console.insert(tk.END, ".........c('')('')..........\n")

    def start_scan_banner(self, target, start, end):
        # print a nice banner to display when starting a scan.
        self.output_console.delete(1.0, "end")
        self.output_console.insert(tk.END, "-" * 28 + "\n")
        self.output_console.insert(tk.END, "Target IP: " + target + "\n")
        self.output_console.insert(tk.END, "Scanning ports:  " + start + " > " + end + "\n")
        self.output_console.insert(tk.END, "Scan started: \n" + str(datetime.now()) + "\n")
        self.output_console.insert(tk.END, "-" * 28 + "\n")

    def validate_input(self, ip, start, end):
        if ip != '' and start != '' and end != '':

            return True
        else:
            return False

    def print_results(self, ports, elapsed):
        self.output_console.insert(tk.END, "Scan Results >>" + "\n")
        self.output_console.insert(tk.END, "elapsed: " + str(elapsed) + "\n")

        if len(ports) > 0:
            for port in range(len(ports)):
                self.output_console.insert(tk.END, "Port {} is open".format(ports[port]) + "\n")
        else:
            self.output_console.insert(tk.END, "Unable to find any open\n ports on target: \n" + str(self.target_input.get()))


    def kill(self):
        sys.exit()

    def save_scan(self):
        if self.scanned:

            ip = self.target_input.get()
            results = self.output_console.get(1.0, "end-1c")
            # print(results)
            now = datetime.now()
            file = tkinter.filedialog.asksaveasfile(defaultextension='.results', initialfile=ip + '_' + str(now.strftime("%d%m%y")))
            file.write(results)
            file.close()