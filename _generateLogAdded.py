import datetime

def generateLogAdd(contacto, hora, minuto, text, isOneTime, gen_id) :
    today = datetime.date.today()
    day_month = today.strftime("%d/%m")

    now = datetime.datetime.now()
    hour_minute = now.strftime("%H:%M")
    
    with open('./logs/generatedLog.txt', 'a') as f:
        if isOneTime :
            text = "Generado con exito mensaje a {} para enviarse a las {}:{}, con el texto:\n'{}.'\nProgramado para una sola vez.\n\nMensaje generado el día {} a las {}.\n ID: {}\n------------------------\n".format(contacto, hora, minuto, text, day_month, hour_minute, gen_id)
        else :
            text = "Generado con exito mensaje a {} para enviarse a las {}:{}, con el texto:\n'{}.'\nProgramado para más de una vez.\n\nMensaje generado el día {} a las {}.\n ID: {}\n------------------------\n".format(contacto, hora, minuto, text, day_month, hour_minute, gen_id)
        f.write(text)