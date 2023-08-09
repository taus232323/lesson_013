import argparse


class TicketMaker:
    def __init__(self, fio, from_location, to, date):
        self.fio = fio
        self.from_location = from_location
        self.to = to
        self.date = date

    def make_ticket(self):
        ticket_info = f"Билет на поезд\nФИО: {self.fio}\nОткуда: {self.from_location}\nКуда: {self.to}\nДата: {self.date}"
        print(ticket_info)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ticket Maker")
    parser.add_argument("--fio", type=str, help="ФИО пассажира")
    parser.add_argument("--from_location", type=str, help="Место отправления")
    parser.add_argument("--to", type=str, help="Место назначения")
    parser.add_argument("--date", type=str, help="Дата")

    args = parser.parse_args()

    if args.fio and args.from_location and args.to and args.date:
        maker = TicketMaker(args.fio, args.from_location, args.to, args.date)
        maker.make_ticket()
    else:
        print("Необходимо указать все аргументы: --fio, --from_location, --to, --date")
