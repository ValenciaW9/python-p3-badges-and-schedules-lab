def badge_maker(name):
    message = "Hello, my name is {name}.".format(name=name)
    return message


def batch_badge_creator(names):
    badge_messages = [badge_maker(name) for name in names]
    return badge_messages


def assign_rooms(names):
    room_assignments = []
    for index, name in enumerate(names):
        room_assignment = "Hello, {name}! You'll be assigned to room {room}!".format(
            name=name, room=index + 1
        )
        room_assignments.append(room_assignment)
    return room_assignments


def printer(names):
    badge_messages = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for message in badge_messages:
        print(message)

    for assignment in room_assignments:
        print(assignment)
