from datetime import datetime, timedelta

class EventNode:
    def __init__(self, event_datetime: datetime, name: str, guests: int, duration_hours: float):
        self.datetime = event_datetime
        self.name = name
        self.guests = guests
        self.duration = duration_hours
        self.left = None
        self.right = None

    def __str__(self):
        return (f"Event('{self.name}', at {self.datetime}, duration={self.duration}h, "
                f"guests={self.guests})")


class EventBST:
    def __init__(self):
        self.root = None

    def _min_node(self, node: EventNode):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _can_schedule_with(self, node: EventNode, new_event: EventNode):
        existing_start = node.datetime
        existing_end = node.datetime + timedelta(hours=node.duration)
        new_start = new_event.datetime
        new_end = new_event.datetime + timedelta(hours=new_event.duration)

        if new_start == existing_start:
            return False

        gap = timedelta(hours=3)
        if new_start < existing_end + gap and existing_start < new_end + gap:
            return False

        return True

    def add_event(self, event_datetime: datetime, name: str, guests: int, duration_hours: float):
        if duration_hours > 5:
            raise ValueError("Duration exceeds 5 hours")

        new_event = EventNode(event_datetime, name, guests, duration_hours)

        def _insert(node: EventNode, new_event: EventNode):
            if node is None:
                return new_event

            if not self._can_schedule_with(node, new_event):
                raise ValueError(f"Conflict with existing event: {node}")

            if new_event.datetime < node.datetime:
                node.left = _insert(node.left, new_event)
            elif new_event.datetime > node.datetime:
                node.right = _insert(node.right, new_event)
            else:
                raise ValueError("Cannot have two events at the same datetime")

            return node

        self.root = _insert(self.root, new_event)

    def cancel_event(self, event_datetime: datetime):
        def _delete(node: EventNode, dt: datetime):
            if node is None:
                return None
            if dt < node.datetime:
                node.left = _delete(node.left, dt)
            elif dt > node.datetime:
                node.right = _delete(node.right, dt)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    succ = self._min_node(node.right)
                    node.datetime = succ.datetime
                    node.name = succ.name
                    node.guests = succ.guests
                    node.duration = succ.duration
                    node.right = _delete(node.right, succ.datetime)
            return node

        self.root = _delete(self.root, event_datetime)

    def display_events_desc(self):
        def _reverse_inorder(node: EventNode):
            if node:
                yield from _reverse_inorder(node.right)
                yield node
                yield from _reverse_inorder(node.left)

        for event in _reverse_inorder(self.root):
            print(event)

    def delete_completed(self, current_time: datetime):
        def _delete_completed(node: EventNode):
            if node is None:
                return None
            end_time = node.datetime + timedelta(hours=node.duration)
            node.left = _delete_completed(node.left)
            node.right = _delete_completed(node.right)
            if end_time < current_time:
                return self._delete_node(node, node.datetime)
            else:
                return node

        self.root = _delete_completed(self.root)

    def _delete_node(self, node: EventNode, dt: datetime):
        def _delete(node: EventNode, dt: datetime):
            if node is None:
                return None
            if dt < node.datetime:
                node.left = _delete(node.left, dt)
            elif dt > node.datetime:
                node.right = _delete(node.right, dt)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    succ = self._min_node(node.right)
                    node.datetime = succ.datetime
                    node.name = succ.name
                    node.guests = succ.guests
                    node.duration = succ.duration
                    node.right = _delete(node.right, succ.datetime)
            return node

        return _delete(node, dt)

from datetime import datetime
if __name__ == "__main__":
    ev = EventBST()
    dt1 = datetime(2025, 9, 20, 10, 0)
    dt2 = datetime(2025, 9, 20, 16, 0)
    dt3 = datetime(2025, 9, 21, 9, 0)
    ev.add_event(dt1, "Morning Meeting", 10, 3)
    ev.add_event(dt2, "Afternoon Workshop", 20, 4)
    try:
        ev.add_event(datetime(2025, 9, 20, 14, 30), "Conflict Event", 5, 2)
    except ValueError as e:
        print("Expected conflict:", e)
    ev.add_event(dt3, "Next day event", 15, 5)
    print("\nAll events descending:")
    ev.display_events_desc()
    ev.cancel_event(dt2)
    print("\nAfter cancelling dt2:")
    ev.display_events_desc()
    now = datetime(2025, 9, 21, 12, 0)
    ev.delete_completed(now)
    print("\nAfter deleting completed by", now)
    ev.display_events_desc()
