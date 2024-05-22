horas_disponibles=["09:00-10:00","11:00-12:00","13:00-14:00","15:00-16:00"]
print("horas_disponibles: ")
for horarios in horas_disponibles:
    print(horarios)
hora_seleccionada=input("selecione un horario de la lista: ")
reserva_lista=True
if reserva_lista:
    print("reserva realizada con exito.")
    costo_alquiler=10
    pago_realizado= True
    if pago_realizado:
        print("pago del alquiler realizado.")
        print("detalles del alquiler.")
        print(f"fecha y hora: {hora_seleccionada}")
        print(f"costo: $ {costo_alquiler}")
    else:
        print("error en el pago del alquiler")
        print("error en la reserva del horario.")



        


    