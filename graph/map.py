LOCATIONS = {
    "A": "Center",
    "B": "University",
    "C": "Hospital",
    "D": "Park",
    "E": "Train Station",
    "F": "Shopping Center",
    "G": "Airport",
}

GRAPH = {
    "A": {
        "B": {
            "distance": 5,
            "time": 8,
            "traffic": 2,
            "difficulty": 1,
        },
        "D": {
            "distance": 7,
            "time": 10,
            "traffic": 3,
            "difficulty": 1,
        },
    },

    "B": {
        "A": {
            "distance": 5,
            "time": 8,
            "traffic": 2,
            "difficulty": 1,
        },
        "C": {
            "distance": 4,
            "time": 7,
            "traffic": 1,
            "difficulty": 1,
        },
        "E": {
            "distance": 6,
            "time": 9,
            "traffic": 2,
            "difficulty": 1,
        },
    },

    "C": {
        "B": {
            "distance": 4,
            "time": 7,
            "traffic": 1,
            "difficulty": 1,
        },
        "G": {
            "distance": 10,
            "time": 15,
            "traffic": 3,
            "difficulty": 2,
        },
    },

    "D": {
        "A": {
            "distance": 7,
            "time": 10,
            "traffic": 3,
            "difficulty": 1,
        },
        "F": {
            "distance": 6,
            "time": 9,
            "traffic": 1,
            "difficulty": 1,
        },
    },

    "E": {
        "B": {
            "distance": 6,
            "time": 9,
            "traffic": 2,
            "difficulty": 1,
        },
        "G": {
            "distance": 7,
            "time": 10,
            "traffic": 2,
            "difficulty": 1,
        },
    },

    "F": {
        "D": {
            "distance": 6,
            "time": 9,
            "traffic": 1,
            "difficulty": 1,
        },
        "G": {
            "distance": 8,
            "time": 12,
            "traffic": 2,
            "difficulty": 1,
        },
    },

    "G": {
        "C": {
            "distance": 10,
            "time": 15,
            "traffic": 3,
            "difficulty": 2,
        },
        "E": {
            "distance": 7,
            "time": 10,
            "traffic": 2,
            "difficulty": 1,
        },
        "F": {
            "distance": 8,
            "time": 12,
            "traffic": 2,
            "difficulty": 1,
        },
    },
}