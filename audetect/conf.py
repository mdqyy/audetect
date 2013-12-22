import os

# Performance settings
MULTITHREAD = True

# Training data locations
class Paths:
    def __init__(self):
        self.DATA_PATH = "data"

    def get_haar_cascade(self):
        return os.path.join(self.DATA_PATH,"haarcascade_frontalface_alt.xml")
    FACE_HAAR_CASCADE = property(get_haar_cascade)

    def get_training_image_path(self):
        return os.path.join(self.DATA_PATH, "images")
    TRAINING_IMAGE_PATH = property(get_training_image_path)

    def get_training_landmark_path(self):
        return os.path.join(self.DATA_PATH, "landmarks")
    TRAINING_LANDMARK_PATH = property(get_training_landmark_path)

    def get_training_output_path(self):
        return os.path.join(self.DATA_PATH, "learned")
    TRAINING_OUTPUT_PATH = property(get_training_output_path)

paths = Paths()

# Gabor filter settings
GABOR_ROTATIONS = [0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]
GABOR_FREQUENCIES = [2, 3.67, 5.33, 7, 8.67, 10.33]

# Learn settings
PATCH_SIZE = 13
GABOR_FILTER_SIZE = 13
FACE_SIZE = 200.0
BOOST_PARAMS = {
    'boost_type': 3, # Gentle AdaBoost
}

# Subset of facial features that are of interest
EXAMINED_POINTS = [17, 21, 22, 26, 31, 35, 48, 54, 57,
                   51, 36, 38, 39, 41, 42, 44, 45, 47]

# Map facial feature points to ROIs
ROI_MAPPING = {
     0: 'left_eyebrow',
     1: 'left_eyebrow',
     2: 'right_eyebrow',
     3: 'right_eyebrow',
     4: 'nose',
     5: 'nose',
     6: 'mouth',
     7: 'mouth',
     8: 'mouth',
     9: 'mouth',
    10: 'left_eye_left_corner',
    11: 'left_eye',
    12: 'left_eye_right_corner',
    13: 'left_eye',
    14: 'right_eye',
    15: 'right_eye',
    16: 'right_eye',
    17: 'right_eye',
}

# Training sets for each AU
AU_POSITIVE_SAMPLES = {
    1: [
        "S014/001",
        "S014/002",
        "S022/001",
        "S022/002",
        "S026/001",
        "S026/002",
        "S032/001",
        "S032/002",
        "S034/001",
        "S034/002",
    ],
    2: [
        "S014/001",
        "S022/001",
        "S026/001",
        "S032/001",
        "S035/001",
        "S037/001",
        "S042/001",
    ],
    4: [
        "S014/002",
        "S014/003",
        "S014/004",
        "S022/002",
        "S022/005",
        "S022/006",
        "S026/003",
        "S026/005",
    ],
    5: [
        "S014/001",
        "S026/001",
        "S032/001",
        "S035/001",
        "S042/001",
        "S044/005",
        "S050/002",
    ],
    6: [
        "S014/005",
        "S026/004",
        "S032/005",
        "S032/006",
        "S034/005",
        "S035/003",
        "S034/005",
    ],
    7: [
        "S014/003",
        "S014/004",
        "S026/005",
        "S032/005",
        "S034/002",
        "S034/003",
        "S034/004",
    ],
    9: [
        "S014/004",
        "S022/006",
        "S026/004",
        "S032/005",
        "S034/003",
        "S034/004",
        "S037/003",
        "S037/004",
        "S037/005",
    ],
    10: [
        "S014/003",
        "S032/002",
        "S042/005",
        "S057/004",
        "S089/003",
        "S107/005",
    ],
    11: [
        "S034/002",
        "S044/002",
        "S045/001",
        "S057/004",
        "S067/003",
        "S070/001",
        "S071/003",
    ],
    12: [
        "S014/001",
        "S014/005",
        "S022/003",
        "S026/006",
        "S032/006",
        "S034/001",
        "S034/005",
        "S035/006",
        "S037/006",
    ],
    15: [
        "S014/002",
        "S022/004",
        "S022/005",
        "S026/002",
        "S026/004",
        "S032/002",
        "S046/001",
        "S050/002",
    ],
    16: [
        "S022/003",
        "S026/006",
        "S055/005",
        "S058/002",
        "S059/001",
        "S067/004",
        "S071/003",
    ],
    17: [
        "S014/002",
        "S014/003",
        "S014/004",
        "S022/004",
        "S022/005",
        "S026/003",
        "S032/002",
        "S032/003",
    ],
    18: [
        "S057/005",
        "S089/003",
        "S092/003",
        "S100/003",
        "S113/003",
    ],
    20: [
        "S022/002",
        "S026/005",
        "S032/004",
        "S034/002",
        "S035/003",
        "S037/005",
        "S042/003",
        "S044/002",
    ],
    23: [
        "S014/003",
        "S032/003",
        "S034/003",
        "S037/003",
        "S037/004",
        "S042/004",
        "S045/005",
        "S052/003",
    ],
    24: [
        "S014/003",
        "S022/005",
        "S026/003",
        "S032/003",
        "S034/003",
        "S037/003",
        "S042/004",
        "S045/002",
        "S045/005",
    ],
    25: [
        "S014/001",
        "S014/005",
        "S022/001",
        "S022/002",
        "S022/003",
        "S026/001",
        "S026/005",
        "S026/006",
        "S032/001",
        "S032/004",
        "S032/005",
        "S032/006",
    ],
    26: [
        "S050/006",
        "S057/001",
        "S064/003",
        "S070/002",
        "S073/001",
        "S073/002",
        "S078/003",
        "S087/001",
        "S088/003",
    ],
    27: [
        "S014/001",
        "S022/001",
        "S026/001",
        "S032/001",
        "S034/001",
        "S035/001",
        "S037/001",
        "S042/001",
        "S044/001",
        "S046/002",
    ],
}

AU_NEGATIVE_SAMPLES = {
    1: [
        "S014/003",
        "S014/004",
        "S022/003",
        "S022/004",
        "S026/003",
        "S026/004",
        "S032/003",
        "S032/004",
        "S034/003",
        "S034/004",
    ],
    2: [
        "S014/002",
        "S022/003",
        "S026/002",
        "S032/003",
        "S035/002",
        "S037/003",
        "S042/002",
    ],
    4: [
        "S014/001",
        "S014/005",
        "S022/001",
        "S022/003",
        "S022/004",
        "S026/001",
        "S026/002",
    ],
    5: [
        "S014/002",
        "S032/003",
        "S032/005",
        "S042/002",
        "S042/003",
        "S045/002",
        "S045/003",
    ],
    6: [
        "S014/001",
        "S026/001",
        "S032/001",
        "S032/002",
        "S034/002",
        "S035/002",
        "S034/001",
    ],
    7: [
        "S014/001",
        "S014/002",
        "S026/001",
        "S032/002",
        "S034/001",
        "S034/003",
        "S034/001",
    ],
    9: [
        "S014/001",
        "S022/003",
        "S026/002",
        "S032/004",
        "S034/001",
        "S034/002",
        "S037/001",
        "S037/002",
        "S037/006",
    ],
    10: [
        "S014/001",
        "S032/001",
        "S042/003",
        "S057/002",
        "S089/001",
        "S107/003",
    ],
    11: [
        "S034/001",
        "S044/001",
        "S045/002",
        "S057/003",
        "S067/002",
        "S070/002",
        "S071/002",
    ],
    12: [
        "S014/002",
        "S014/004",
        "S022/001",
        "S026/003",
        "S032/003",
        "S034/002",
        "S034/003",
        "S035/001",
        "S037/002",
    ],
    15: [
        "S014/001",
        "S022/002",
        "S022/003",
        "S026/001",
        "S026/003",
        "S032/001",
        "S046/002",
        "S050/001",
    ],
    16: [
        "S022/001",
        "S026/003",
        "S055/004",
        "S058/001",
        "S059/002",
        "S067/003",
        "S071/002",
    ],
    17: [
        "S014/001",
        "S014/005",
        "S022/001",
        "S022/002",
        "S022/003",
        "S026/002",
        "S032/001",
        "S032/004",
    ],
    20: [
        "S022/001",
        "S026/003",
        "S032/002",
        "S034/001",
        "S035/002",
        "S037/003",
        "S042/002",
        "S044/001",
    ],
    23: [
        "S014/004",
        "S032/002",
        "S034/001",
        "S037/002",
        "S037/003",
        "S042/002",
        "S045/004",
        "S052/002",
    ],
    24: [
        "S014/002",
        "S022/004",
        "S026/002",
        "S032/002",
        "S034/001",
        "S037/001",
        "S042/003",
        "S045/001",
        "S045/003",
    ],
    25: [
        "S014/002",
        "S014/003",
        "S022/004",
        "S022/005",
        "S022/006",
        "S026/002",
        "S026/003",
        "S026/004",
        "S032/002",
        "S032/003",
        "S032/004",
        "S034/003",
    ],
    26: [
        "S050/003",
        "S057/002",
        "S064/002",
        "S070/001",
        "S073/003",
        "S073/004",
        "S078/001",
        "S087/002",
        "S088/002",
    ],
    27: [
        "S014/002",
        "S022/003",
        "S026/002",
        "S032/003",
        "S034/002",
        "S035/003",
        "S037/002",
        "S042/003",
        "S044/002",
        "S046/001",
    ],

}

AU_LABELS = {
     1: "Inner Brow Raiser",
     2: "Outer Brow Raiser",
     4: "Brow Lowerer",
     6: "Cheek Raiser",
     7: "Lid Tightener",
     9: "Nose Wrinkler",
    10: "Upper Lip Raiser",
    11: "Nasolabial Deepener",
    12: "Lip Corner Puller",
    15: "Lip Corner Depressor",
    16: "Lower Lip Depressor",
    17: "Chin Raiser",
    20: "Lip Stretcher",
    23: "Lip Tightener",
    24: "Lip Pressor",
    25: "Lips Part",
    26: "Jaw Drop",
    27: "Mouth Stretch",
}

AU_ZERO_INDEX_MAPPING = [1, 2, 4, 6, 7, 9, 10, 11, 12, 15, 16, 17,
                         20, 23, 24, 25, 26, 27]

AU_LOCATIONS = {
     1: ("left_eyebrow", "right_eyebrow"),
     2: ("left_eyebrow", "right_eyebrow"),
     4: ("left_eyebrow", "right_eyebrow"),
     5: ("left_eye", "right_eye"),
     6: ("left_eye", "right_eye"),
     7: ("left_eye", "right_eye"),
     9: ("nose",),
    10: ("mouth",),
    11: ("nose",),
    12: ("mouth",),
    15: ("mouth",),
    16: ("mouth",),
    17: ("mouth",),
    20: ("mouth",),
    23: ("mouth",),
    24: ("mouth",),
    25: ("mouth",),
    26: ("mouth",),
    27: ("mouth",),
}
