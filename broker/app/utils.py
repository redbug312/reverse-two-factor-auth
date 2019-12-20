def random_icon(seed):
    return '%s %s' % (icon_colors[seed % len(icon_colors)],
                      icon_shapes[seed % len(icon_shapes)])


icon_colors = [
    'red', 'orange', 'yellow', 'olive', 'green',
    'teal', 'blue', 'violet', 'purple', 'pink',
    'brown', 'grey', 'black']

icon_shapes = [
    'ambulance', 'anchor', 'balance scale', 'bath', 'bed',
    'beer', 'bell', 'bell slash', 'bicycle', 'binoculars',
    'birthday cake', 'blind', 'bomb', 'book', 'bookmark',
    'briefcase', 'building', 'car', 'coffee', 'crosshairs',
    'dollar sign', 'eye', 'eye slash', 'fighter jet', 'fire',
    'fire extinguisher', 'flag', 'flag checkered', 'flask', 'gamepad',
    'gavel', 'gift', 'glass martini', 'globe', 'graduation cap',
    'h square', 'heart', 'heartbeat', 'home', 'hospital',
    'images', 'industry', 'info', 'info circle',
    'key', 'leaf', 'lemon', 'life ring', 'lightbulb',
    'location arrow', 'low vision', 'magnet', 'male', 'map',
    'map marker', 'map marker alternate', 'map pin', 'map signs', 'medkit',
    'money bill alternate', 'motorcycle', 'music', 'newspaper', 'paw',
    'phone', 'phone square', 'phone volume', 'plane', 'plug',
    'plus', 'plus square', 'print', 'recycle', 'road',
    'rocket', 'search', 'search minus', 'search plus', 'ship',
    'shopping bag', 'shopping basket', 'shopping cart', 'shower', 'street view',
    'subway', 'suitcase', 'tag', 'tags', 'taxi',
    'thumbtack', 'ticket alternate', 'tint', 'train', 'tree',
    'trophy', 'truck', 'tty', 'umbrella', 'university',
    'utensil spoon', 'utensils', 'wheelchair', 'wifi', 'wrench',
    'copy link']
