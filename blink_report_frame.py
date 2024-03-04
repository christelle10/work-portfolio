import customtkinter as ctk
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
from ttkbootstrap.constants import *
import sqlite3
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.ticker import MaxNLocator
from datetime import datetime
import re
import mplcursors  # Import mplcursors library
from collections import defaultdict
from styling import WhiteButton, SubheadingSettings

#feb5 note: test processdata for tab3
class BlinkReportFrame(ctk.CTkFrame):
    def __init__(self, master=None, main_content=None, username="", **kwargs):
        super().__init__(master, **kwargs)
        self.main_content = main_content
        self.signed_username = username
        self.tab3_chosen_start_date = self.get_first_entry_date()
        self.tab3_chosen_end_date = self.get_last_entry_date()
               
        
        self.tab1_chosen_date = self.get_first_entry_date()
        self.tab2_chosen_date = self.get_first_entry_date()
        self.create_tabs()
        self.frame1 = ctk.CTkFrame(self.tab1, corner_radius=10)
        self.frame1.configure(fg_color='#FFFFFF')
        self.frame1.pack(side="top", fill="x")

        self.frame2 = ctk.CTkFrame(self.tab2, corner_radius=10)
        self.frame2.configure(fg_color='#FFFFFF')
        self.frame2.pack(side="top", fill="x")

        self.frame3 = ctk.CTkFrame(self.tab3, corner_radius=10)
        self.frame3.configure(fg_color='#FFFFFF')
        self.frame3.pack(side="top", fill="x")
        
        self.current_canvas = None

        # Automatically plot the first tab
        

        #tab1
        
        
        self.date_entry1 = ttk.DateEntry(master=self.frame1, style='flatly')
        self.date_entry1.grid(row=0, column=0, padx=(600, 10), pady=(30,30))
        get_date1 = WhiteButton(self.frame1, text='Get Date', command=self.datey1)
        get_date1.grid(row=0, column=1, padx=(20, 10), pady=(30,30))
        self.update_graph_bt1 = WhiteButton(self.frame1, text='Plot Data', command=self.update_graph)
        self.update_graph_bt1.configure(state='disabled')
        self.update_graph_bt1.grid(row=0, column=2, padx=(20, 10), pady=(30,30))

        #tab2
        self.date_entry2 = ttk.DateEntry(master=self.frame2)
        self.date_entry2.grid(row=0, column=0, padx=(600, 10), pady=(30,30))
        get_date2 = WhiteButton(self.frame2, text='Get Date', command=self.datey2)
        get_date2.grid(row=0, column=1, padx=(20, 10), pady=(30,30))
        self.update_graph_bt2 = WhiteButton(self.frame2, text='Plot Data', command=self.update_graph2)
        self.update_graph_bt2.configure(state='disabled')
        self.update_graph_bt2.grid(row=0, column=2, padx=(20, 10), pady=(30,30))

        #tab3
        self.date_entry3 = ctk.CTkFrame(master=self.frame3)
        self.date_entry3.configure(fg_color='#ffffff')
        self.date_entry3.pack(pady=10)
        self.start_date_entry3_label = SubheadingSettings(master=self.date_entry3, text="Start Date:")
        self.start_date_entry3_label.pack(side=tk.LEFT, pady=10, padx=10)
        
        self.start_date_entry3 = ttk.DateEntry(master=self.date_entry3)
        self.start_date_entry3.pack(side=tk.LEFT, pady=10, padx=10)

        self.end_date_entry3_label = SubheadingSettings(master=self.date_entry3, text="End Date:")
        self.end_date_entry3_label.pack(side=tk.LEFT, pady=10, padx=10)
        self.end_date_entry3 = ttk.DateEntry(master=self.date_entry3)
        self.end_date_entry3.pack(side=tk.LEFT, pady=10, padx=10)       
        get_date2 = WhiteButton(self.date_entry3, text='Get Date', command=self.datey3)
        get_date2.pack(side=tk.LEFT, pady=10, padx=10)

        self.update_graph_bt3 = WhiteButton(self.date_entry3, text='Plot Data', command=self.update_graph3)
        self.update_graph_bt3.configure(state='disabled')
        self.update_graph_bt3.pack(side=tk.LEFT, pady=10, padx=10)
        #self.plot_data("data_blink_m")

    def get_first_entry_date(self):
        try:
            conn = sqlite3.connect("C:\\Users\\dojac\\Desktop\\Ocu Aspida Desktop\\data.db")
            cursor = conn.cursor()

            # Query to get the minimum date for the specified username
            cursor.execute("""
                SELECT MIN(blink_recorded_date) as min_date
                FROM blink_data
                JOIN users ON user_id_blink = user_id
                WHERE username=?
            """, (self.signed_username,))

            result = cursor.fetchone()
            if result:
                min_date = result[0]
                return min_date
            else:
                return None
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            conn.close()
    
    def get_last_entry_date(self):
        try:
            conn = sqlite3.connect("C:\\Users\\dojac\\Desktop\\Ocu Aspida Desktop\\data.db")
            cursor = conn.cursor()

            # Query to get the minimum date for the specified username
            cursor.execute("""
                SELECT MAX(blink_recorded_date) as max_date
                FROM blink_data
                JOIN users ON user_id_blink = user_id
                WHERE username=?
            """, (self.signed_username,))

            result = cursor.fetchone()
            if result:
                max_date = result[0]
                return max_date
            else:
                return None
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            conn.close()
    def update_graph(self):
        # Fetch new data based on the updated date
        data = self.fetch_data_from_database("data_blink_m")
        if data:
            # Clear existing graph
            if self.current_canvas:
                self.current_canvas.get_tk_widget().pack_forget()
                self.current_canvas.get_tk_widget().destroy()

            # Plot the updated graph
            self.plot_graph(data, "data_blink_m")
        else:
            messagebox.showinfo("Info", "No Data Available for Plotting")
    def update_graph2(self):
        # Fetch new data based on the updated date
        data = self.fetch_data_from_database("data_blink_h")
        if data:
            # Clear existing graph
            if self.current_canvas:
                self.current_canvas.get_tk_widget().pack_forget()
                self.current_canvas.get_tk_widget().destroy()

            # Plot the updated graph
            self.plot_graph(data, "data_blink_h")
        else:
            messagebox.showinfo("Info", "No Data Available for Plotting")
    
    def update_graph3(self):
        # Fetch new data based on the updated date
        data = self.fetch_data_from_database("data_blink_d")
        if data:

            # Clear existing graph
            if self.current_canvas:
                self.current_canvas.get_tk_widget().pack_forget()
                self.current_canvas.get_tk_widget().destroy()

            # Plot the updated graph
            self.plot_graph(data, "data_blink_d")
        else:
            messagebox.showinfo("Info", "No Data Available for Plotting")

    def datey1(self):# Grab The Date
        chosen_date_str = self.date_entry1.entry.get()
        self.update_graph_bt1.configure(state='normal')
        messagebox.showinfo('Info', 'Date has been updated successfully.')
        try:
            # Parse the current format (assuming it is "%d/%m/%Y")
            chosen_date_obj = datetime.strptime(chosen_date_str, "%d/%m/%Y")
            # Format into the desired format ("%Y-%m-%d")
            self.tab1_chosen_date = chosen_date_obj.strftime("%Y-%m-%d")
            #self.update_graph()
        except ValueError:
            print("Invalid date format")

    def datey2(self):# Grab The Date
        chosen_date_str = self.date_entry2.entry.get()
        self.update_graph_bt2.configure(state='normal')
        messagebox.showinfo('Info', 'Date has been updated successfully.')
        try:
            # Parse the current format (assuming it is "%d/%m/%Y")
            chosen_date_obj = datetime.strptime(chosen_date_str, "%d/%m/%Y")
            # Format into the desired format ("%Y-%m-%d")
            self.tab2_chosen_date = chosen_date_obj.strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format")

    def datey3(self):# Grab The Date
        chosen_date_str1 = self.start_date_entry3.entry.get()
        chosen_date_str2 = self.end_date_entry3.entry.get()
        self.update_graph_bt3.configure(state='normal')
        messagebox.showinfo('Info', 'Date has been updated successfully.')
        try:
            # Parse the current format (assuming it is "%d/%m/%Y")
            chosen_date_obj1 = datetime.strptime(chosen_date_str1, "%d/%m/%Y")
            chosen_date_obj2 = datetime.strptime(chosen_date_str2, "%d/%m/%Y")

            if chosen_date_obj1 > chosen_date_obj2:
                messagebox.showerror("Error", "Start date should be before End date. Please try again.")
                return
            # Format into the desired format ("%Y-%m-%d")
            self.tab3_chosen_start_date = chosen_date_obj1.strftime("%Y-%m-%d")
            self.tab3_chosen_end_date = chosen_date_obj2.strftime("%Y-%m-%d")
            
        except ValueError:
            print("Invalid date format")
    
    def create_tabs(self):
        self.tabControl = ttk.Notebook(self)  # Use self as the parent

        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='Data Blink (Minutes)')

        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab2, text='Data Blink (Hours)')

        self.tab3 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab3, text='Data Blink (Days)')

        self.tabControl.pack(expand=1, fill="both")
         
    def process_data_tab2(self, data):
        # Create a dictionary to store the total blink count and count of blinks per hour
        hour_data = defaultdict(lambda: {'count': 0, 'total_blinks': 0})

        # Process each row of data
        for row in data:
            blink_count = row[0]
            recorded_time = str(row[2])
            

            try:
            # Extract the hour from the recorded time
                dt_object = datetime.strptime(recorded_time, '%Y-%m-%d %H:%M:%S.%f')
                rounded_hour = dt_object.replace(minute=0, second=0, microsecond=0)
                hour = rounded_hour.hour

                hour_data[hour]['count'] += 1
                hour_data[hour]['total_blinks'] += blink_count
            except ValueError as e:
                print(f"Error processing timestamp {recorded_time}: {e}")
        
        hours = list(range(1, 25))
        # Calculate the average blink count per hour and create a list of hours
        average_blink_count_per_hour = {hour: None for hour in hours}
        
        
        for hour, data in hour_data.items():
            if data['count'] > 0:
                average_blink_count_per_hour[hour] = round(data['total_blinks'] / data['count'])
            else:
                average_blink_count_per_hour[hour] = None
            
        
        return hours, average_blink_count_per_hour
    
    def process_data_tab3(self, data): 
        # Create a dictionary to store the total blink count and count of blinks per minute for each date
        date_data = defaultdict(lambda: {'count': 0, 'total_blinks': 0})

        # Process each row of data
        for row in data:
            blink_count = row[0]
            recorded_time = str(row[2])

            try:
                # Extract the date from the recorded time
                dt_object = datetime.strptime(recorded_time, '%Y-%m-%d %H:%M:%S.%f')
                date = dt_object.date()

                date_str = date.strftime('%Y-%m-%d')

                date_data[date_str]['count'] += 1
                date_data[date_str]['total_blinks'] += blink_count
            except ValueError as e:
                print(f"Error processing timestamp {recorded_time}: {e}")

        # Calculate the average blink count per minute for each date
        average_blink_count_per_date = {}
        for date, data in date_data.items():
            if data['count'] > 0:
                average_blink_count_per_date[date] = round(data['total_blinks'] / data['count'])
            else:
                average_blink_count_per_date[date] = None
        
        return average_blink_count_per_date

    def on_tab_change(self, event):
        current_tab = self.tabControl.select()
        self.tab_text = self.tabControl.tab(current_tab, "text")

        if self.tab_text == 'Data Blink (Minutes)':
            self.plot_data("data_blink_m")
        elif self.tab_text == 'Data Blink (Hours)':
            self.plot_data("data_blink_h")
        elif self.tab_text == 'Data Blink (Days)':
            self.plot_data("data_blink_d")

    def plot_data(self, table_name):
        try:
            data = self.fetch_data_from_database(table_name)
            if data:
                self.plot_graph(data, table_name)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def fetch_data_from_database(self, table_name):
        conn = sqlite3.connect("C:\\Users\\dojac\\Desktop\\Ocu Aspida Desktop\\data.db")  # Replace with your actual database name
        cursor = conn.cursor()
        if self.tabControl.index(self.tabControl.select()) == 0:
            cursor.execute("""
    SELECT number_of_blinks_per_minute, username, blink_recorded_time, blink_recorded_date
    FROM blink_data
    JOIN users ON user_id_blink = user_id
    WHERE username=? AND blink_recorded_date=?
""", (self.signed_username, self.tab1_chosen_date))
        
        elif self.tabControl.index(self.tabControl.select()) == 1:
            cursor.execute("""
    SELECT number_of_blinks_per_minute, username, blink_recorded_time
    FROM blink_data
    JOIN users ON user_id_blink = user_id
    WHERE username=? AND blink_recorded_date=?
""", (self.signed_username, self.tab2_chosen_date))
        
        elif self.tabControl.index(self.tabControl.select()) == 2:
            cursor.execute("""
            SELECT number_of_blinks_per_minute, username, blink_recorded_time, blink_recorded_date
            FROM blink_data
            JOIN users ON user_id_blink = user_id
            WHERE username=? AND blink_recorded_date BETWEEN ? AND ?
        """, (self.signed_username, self.tab3_chosen_start_date, self.tab3_chosen_end_date))
        data = cursor.fetchall()
        return data
    
    def plot_graph(self, data, table_name):
        if not data:
            messagebox.showinfo("No Data Available for Plotting", "You did not turn Ocu-Aspida during this time.")
            return
        
        fig, ax = plt.subplots(figsize=(3, 3), tight_layout=True)  # Set the figure size to a reasonable value  # Set the figure size to a reasonable value
        fig.subplots_adjust(left=0.1, right=0.95)  # Adjust left and right margins

        

        blink_counts = [row[0] for row in data]
        usernames = [row[1] for row in data]

        #------tab 2 configs------------
        hours, average_blink_count_per_hour = self.process_data_tab2(data)
        
        avg_blink_counts = [value if value is not None else 0 for value in average_blink_count_per_hour.values()]
        bar_colors = ['#FF7A66' if count <= 7 else 'green' for count in blink_counts]
        if self.tabControl.index(self.tabControl.select()) == 0: #tab1
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d %H:%M:%S'))
            blink_times = [re.search(r'\d{2}:\d{2}:\d{2}', row[2]).group() for row in data]
            blink_dates = [row[3] for row in data]
            bars = ax.bar(blink_times, blink_counts, color=bar_colors)
            ax.set_xlabel(f"Blink Rate Data for: {str(self.tab1_chosen_date)}")
            ax.set_ylabel("Blink Count")
            ax.set_yticks(range(0, 21))  # Set y-axis ticks from -1 to 20
            ax.set_yticklabels([str(i) for i in range(21)])  # Set y-axis labels, including 'No Data'
            ax.set_xticks(blink_times)
            ax.set_xticklabels(blink_dates, rotation=45, ha='right')
            
        elif self.tabControl.index(self.tabControl.select()) == 1: #tab 2: 
            bars = ax.bar(hours, avg_blink_counts, color=['#FF7A66' if count <= 7 else 'green' for count in avg_blink_counts])
            ax.set_xlabel(f"Blink Rate Data for: {str(self.tab2_chosen_date)}")
            ax.set_ylabel("Average Blink Count")
              # Set y-axis ticks from -1 to 20
            ax.set_yticks(range(0, 21))  # Set y-axis ticks from -1 to 20
            ax.set_yticklabels([str(i) for i in range(21)])  # Set y-axis labels, including 'No Data'
            blink_times = hours
            # Set x-axis ticks and labels
            ax.set_xticks(hours)
            ax.set_xticklabels([f"{hour:02d}:00" if average_blink_count_per_hour[hour] is not None else f"{hour:02d}:00" for hour in hours], rotation=45, ha='right')
            for label in ax.get_xticklabels():
                hour = int(label.get_text()[:2])
                if average_blink_count_per_hour[hour] is None:
                    label.set_color('blue')
                else:
                    label.set_color('black')

        elif self.tabControl.index(self.tabControl.select()) == 2: #plot tab 3  
                
            data_tab3 = self.process_data_tab3(data)
            dates = list(data_tab3.keys())
            avg_counts = list(data_tab3.values())
            bars = ax.bar(dates, avg_counts, color=['#FF7A66' if count <= 7 else 'green' for count in avg_counts])
            ax.set_xlabel(f"Blink Rate Data for: {str(self.tab3_chosen_start_date)} to {str(self.tab3_chosen_start_date)}")
            ax.set_ylabel("Average Blink Count")
            ax.set_yticks(range(0, 21))  # Set y-axis ticks from 0 to 20
            ax.set_yticklabels([str(i) for i in range(21)])  # Set y-axis labels, including 'No Data'
            ax.set_xticks(dates)
            ax.set_xticklabels(dates, rotation=45, ha='right')
            for label in ax.get_xticklabels():
                label.set_color('black')  # Set x-axis labels color to black
        
        
        
        ##insert plotting of graphs here
       
        for label in ax.get_yticklabels():
            if 0 <= int(label.get_text()) <= 8:
                label.set_color('red')
            
            

        # Set y-axis labels 0-5 to red
        
        if self.tabControl.index(self.tabControl.select()) == 0:
            ax.set_xticklabels(blink_times)
        
            

        def on_hover_blink(sel):
            if self.tabControl.index(self.tabControl.select()) == 0:
                index = sel.index
                blink_count = blink_counts[index]
                username = usernames[index]
                blink_time = blink_times[index]
                sel.annotation.set_text(f"Blink Count: {blink_count}\nUsername: {username}\nBlink Time: {blink_time}")
            elif self.tabControl.index(self.tabControl.select()) == 1:
                index = sel.index
                hour = hours[index]
                avg_blink_count = avg_blink_counts[index]
                sel.annotation.set_text(f"Hour: {hour}:00 \nAverage Blink Count: {avg_blink_count}")
            elif self.tabControl.index(self.tabControl.select()) == 2:
                index = sel.index
                date = dates[index]
                avg_blink_count = avg_counts[index]
                sel.annotation.set_text(f"Date: {date}\nAverage Blink Count: {avg_blink_count}")

        cursor = mplcursors.cursor(hover=True)
        cursor.connect("add", on_hover_blink)

        if self.current_canvas:
            self.current_canvas.get_tk_widget().pack_forget()
            self.current_canvas.get_tk_widget().destroy()

        if self.tabControl.index(self.tabControl.select()) == 0: #tab1
            self.current_canvas = FigureCanvasTkAgg(fig, master=self.tab1) 
        elif self.tabControl.index(self.tabControl.select()) == 1: #tab2
            self.current_canvas = FigureCanvasTkAgg(fig, master=self.tab2)
        else:  # tab3
            self.current_canvas = FigureCanvasTkAgg(fig, master=self.tab3)
        canvas_widget = self.current_canvas.get_tk_widget()
        canvas_widget.pack(side="left", fill="both", expand=True)
