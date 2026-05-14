from nicegui import ui

questions = [
    {"question": "Quelle est la capitale de la France ?", "reponse": "paris"},
    {"question": "Combien font 7 × 8 ?", "reponse": "56"},
]

index = {"current": 0}

def verifier(input_field, label_resultat):
    q = questions[index["current"]]
    if input_field.value.strip().lower() == q["reponse"]:
        label_resultat.set_text("✅ Bonne réponse !")
    else:
        label_resultat.set_text(f'❌ Mauvais, la réponse était : {q["reponse"]}')
    
    # Passer à la question suivante
    index["current"] = (index["current"] + 1) % len(questions)
    label_question.set_text(questions[index["current"]]["question"])
    input_field.set_value('')  # Vider le champ

with ui.card().classes('w-96 mx-auto mt-10'):
    label_question = ui.label(questions[0]["question"]).classes('text-lg font-bold')
    champ = ui.input(placeholder='Ta réponse...').classes('w-full')
    label_resultat = ui.label('')
    ui.button('Valider', on_click=lambda: verifier(champ, label_resultat))

ui.run()