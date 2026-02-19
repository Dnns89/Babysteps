import random
from models import exercises


def get_exercises_by_categories(selected_categories, max_difficulty=0):
    """
    Filtert die globale Übungsliste nach Kategorien und Schwierigkeitsgrad.
    """
    if not selected_categories:
        pool = exercises.copy()
    else:
        # Übung wird aufgenommen, wenn mindestens eine gewählte Kategorie passt
        pool = [ex for ex in exercises if any(cat in ex.categories for cat in selected_categories)]

    if max_difficulty > 0:
        pool = [ex for ex in pool if ex.difficulty <= max_difficulty]

    return pool


def generate_plan_by_count(pool, count):
    """
    Erstellt einen Plan mit einer festen Anzahl an Übungen.
    """
    available = pool.copy()
    random.shuffle(available)

    plan = []
    total_duration = 0

    # Sicherstellen, dass wir nicht mehr anfordern als da sind
    limit = min(count, len(available))

    while len(plan) < limit:
        ex = available.pop()
        plan.append(ex)
        total_duration += ex.duration * 2  # Spieler A + B

    return plan, total_duration


def generate_plan_by_time(pool, max_time):
    """
    Erstellt einen Plan, der die vorgegebene Zeit so gut wie möglich füllt.
    """
    available = pool.copy()
    random.shuffle(available)

    plan = []
    total_duration = 0

    for ex in available:
        ex_total = ex.duration * 2
        if total_duration + ex_total <= max_time:
            plan.append(ex)
            total_duration += ex_total

    return plan, total_duration