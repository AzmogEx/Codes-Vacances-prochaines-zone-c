import datetime
import tkinter as tk

def count_down():
    # date de début des vacances scolaires pour la zone C
    vacances = datetime.datetime(2023, 2, 18)

    # date d'aujourd'hui
    aujourdhui = datetime.datetime.now()

    # calculer la différence entre les deux dates
    diff = vacances - aujourdhui

    # afficher le compte à rebours
    days = diff.days
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    temps =  "{} jours, {} heures, {} minutes et {} secondes jusqu'aux prochaines vacances scolaires.".format(days, hours, minutes, seconds)
    label.config(text = temps)
    label.after(1000, count_down)

# Création de la fenêtre
root = tk.Tk()
root.title("Compte à rebours vacances scolaires zone C")

# Création de label
label = tk.Label(root, font = ("Arial", 20))
label.pack()

# Appel de la fonction count_down
count_down()

root.mainloop()
