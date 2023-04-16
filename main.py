from cars import Sedan, Hatchback, Pickup
from engines import GasEngine, DieselEngine, ElectricalEngine
from gearboxes import ManualTransmission, AutomaticTransmission, RoboticTransmission, InvalidSpeed


def execute_application():
    aveo = Hatchback("Checvrolet", "aveo-2", "2013")
    engine_bs14 = GasEngine("BS-14", "102", "бензин")
    trans_mr51 = ManualTransmission("MR-5.1", "ручная", 5)

    aveo.print_failure_status(engine_bs14)
    aveo.print_speed_status(trans_mr51)

    engine_bs14.add_error("A-022")
    try:
        trans_mr51.gear_up()
    except InvalidSpeed as e:
        print(e)

    aveo.print_failure_status(engine_bs14)
    aveo.print_speed_status(trans_mr51)

    print("----------------")

    passat = Sedan("VW", "Passat B-7", "2018")
    engine_mpe205 = ElectricalEngine("MPE-205", "205", "электричество")
    trans_ev8 = RoboticTransmission("EV-8", "роботизированная", 8)

    passat.print_failure_status(engine_mpe205)
    passat.print_speed_status(trans_ev8)

    engine_mpe205.add_error("F-1034")
    try:
        trans_ev8.gear_down()
    except InvalidSpeed as e:
        print(e)

    passat.print_failure_status(engine_mpe205)
    passat.print_speed_status(trans_ev8)


if __name__ == "__main__":
    execute_application()
