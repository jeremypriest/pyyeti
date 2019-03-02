import numpy as np
from pyyeti import stats
from nose.tools import *


def test_ksingle():
    v = stats.ksingle(
        [0.95, 0.96, 0.97, 0.98, 0.99],
        [[0.50], [0.75], [0.90], [0.95]],
        [[[2]], [[5]], [[10500]]],
    )
    # answers from CAM:
    s = np.array(
        [
            # n = 2: ksingle(ones(4, 1)*(.95:.01:.99),
            #                [.5; .75; .9; .95]*ones(1, 5), 2)
            [
                [
                    2.3387267270021,
                    2.5004445468937,
                    2.6990141016375,
                    2.9623892315012,
                    3.3759678335076,
                ],
                [
                    5.1215097349665,
                    5.4536820957809,
                    5.8629283483735,
                    6.4077255189944,
                    7.2668686208323,
                ],
                [
                    13.0897418707900,
                    13.9260983982938,
                    14.9573139498444,
                    16.3312483458830,
                    18.5000774765598,
                ],
                [
                    26.2596737593652,
                    27.9340655790353,
                    29.9987853609414,
                    32.7500210299024,
                    37.0935812446344,
                ],
            ],
            # n = 5:
            [
                [
                    1.7792826967494,
                    1.8951820551046,
                    2.0376947576830,
                    2.2271608515375,
                    2.5257695789774,
                ],
                [
                    2.4633832336159,
                    2.6110093695996,
                    2.7931686038089,
                    3.0362782810357,
                    3.4212048208534,
                ],
                [
                    3.3998339417066,
                    3.5941836186675,
                    3.8344617395268,
                    4.1558275948177,
                    4.6659821742004,
                ],
                [
                    4.2026807172416,
                    4.4384373472151,
                    4.7301312529540,
                    5.1205971501181,
                    5.7410844875278,
                ],
            ],
            # n = 10500:
            [
                [
                    1.6449002334613,
                    1.7507360934091,
                    1.8808478455894,
                    2.0538087733481,
                    2.3264166312809,
                ],
                [
                    1.6550298057337,
                    1.7612460453008,
                    1.8918378685979,
                    2.0654554523237,
                    2.3391337176469,
                ],
                [
                    1.6642024262338,
                    1.7707642658358,
                    1.9017921431697,
                    2.0760060040048,
                    2.3506559617324,
                ],
                [
                    1.6697173372285,
                    1.7764874871483,
                    1.9077781394215,
                    2.0823512561092,
                    2.3575865187188,
                ],
            ],
        ]
    )

    assert abs(s - v).max() < 1e-8


def test_kdouble():
    v = stats.kdouble(
        [0.95, 0.96, 0.97, 0.98, 0.99],
        [[0.50], [0.75], [0.90], [0.95]],
        [[[2]], [[5]], [[10500]]],
    )

    # answers from CAM:
    s = np.array(
        [
            # n = 2: kdouble(ones(4, 1)*(.95:.01:.99),
            #                [.5; .75; .9; .95]*ones(1, 5), 2)
            [
                [
                    3.5025641700606,
                    3.6569766929300,
                    3.8473517062397,
                    4.1011651012123,
                    4.5024646553985,
                ],
                [
                    7.4141612722213,
                    7.7410187661655,
                    8.1440009764399,
                    8.6812683474313,
                    9.5307316174092,
                ],
                [
                    18.8000820553148,
                    19.6288943081005,
                    20.6507359354705,
                    22.0130843238344,
                    24.1670675718649,
                ],
                [
                    37.6744541754207,
                    39.3353538005251,
                    41.3830749461892,
                    44.1131551542096,
                    48.4296332915805,
                ],
            ],
            # n = 5:
            [
                [
                    2.3369393771603,
                    2.4465209332565,
                    2.5821447377181,
                    2.7637654835860,
                    3.0525193486800,
                ],
                [
                    3.0879030011960,
                    3.2326980349278,
                    3.4119038615417,
                    3.6518875135465,
                    4.0334309696349,
                ],
                [
                    4.1515418193220,
                    4.3462120008448,
                    4.5871458913088,
                    4.9097927383327,
                    5.4227601512424,
                ],
                [
                    5.0787066669647,
                    5.3168525876339,
                    5.6115943026523,
                    6.0062979487601,
                    6.6338264991784,
                ],
            ],
            # n = 10500:
            [
                [
                    1.9601195449673,
                    2.0539119140928,
                    2.1702626141150,
                    2.3265325112384,
                    2.5760337391670,
                ],
                [
                    1.9692789556380,
                    2.0635096055962,
                    2.1804039989080,
                    2.3374041270864,
                    2.5880712452360,
                ],
                [
                    1.9775838363101,
                    2.0722118775578,
                    2.1895992401288,
                    2.3472614722342,
                    2.5989857085227,
                ],
                [
                    1.9825819035879,
                    2.0774491040095,
                    2.1951331467641,
                    2.3531938481676,
                    2.6055542823484,
                ],
            ],
        ]
    )

    assert abs(s - v).max() < 1e-8


def test_order_stats():
    r = np.arange(1, 5)
    p = np.array([0.95, 0.97725, 0.99, 0.9973, 0.99865])
    c = np.array([0.50, 0.90])
    n = np.array([1000, 2000, 3000])

    r_table = stats.order_stats("r", p=0.99, c=c, n=n.reshape(-1, 1))
    # comparison answers are from CAM:
    assert np.all(r_table == [[10, 6], [20, 14], [30, 23]])

    n = np.array([100, 200, 300])
    p_table = stats.order_stats(
        "p", c=c.reshape(1, 1, -1), n=n.reshape(1, -1, 1), r=r.reshape(-1, 1, 1)
    )
    s = np.array(
        [
            [
                [0.993092495402498, 0.977237221069625],
                [0.996540262845167, 0.988553094699397],
                [0.997692176527023, 0.992354096170330],
            ],
            [
                [0.983273329531057, 0.961660502512008],
                [0.991622480612251, 0.980691361823315],
                [0.994411830400318, 0.987096551596171],
            ],
            [
                [0.973349324730802, 0.947654709557887],
                [0.986652204730905, 0.973608649656815],
                [0.991096472042914, 0.982356936890818],
            ],
            [
                [0.963402518577899, 0.934414248810156],
                [0.981670510979568, 0.966902529937789],
                [0.987773497888500, 0.977867058994108],
            ],
        ]
    )

    assert abs(p_table - s).max() < 1e-9

    n_table = stats.order_stats(
        "n",
        c=0.90,
        r=np.arange(1, 13).reshape(-1, 1),
        p=[0.95, 0.97725, 0.99, 0.9973, 0.99865],
    )
    s = np.array(
        [
            [45, 101, 230, 852, 1705],
            [77, 170, 388, 1440, 2880],
            [105, 233, 531, 1970, 3941],
            [132, 292, 667, 2473, 4947],
            [158, 350, 798, 2959, 5920],
            [184, 406, 926, 3433, 6868],
            [209, 461, 1051, 3899, 7800],
            [234, 516, 1175, 4358, 8717],
            [258, 569, 1297, 4811, 9624],
            [282, 622, 1418, 5259, 10521],
            [306, 675, 1538, 5704, 11410],
            [330, 727, 1658, 6145, 12293],
        ]
    )
    assert abs(n_table - s).max() < 1e-9

    p = np.array([0.95, 0.97725])
    r = np.array([3, 5])
    c_table = stats.order_stats(
        "c", p=p.reshape(1, 1, -1), n=n.reshape(1, -1, 1), r=r.reshape(-1, 1, 1)
    )
    s = np.array(
        [
            [
                [0.881737018814879, 0.398156949210935],
                [0.997663705809936, 0.835164122880967],
                [0.999970732474034, 0.967583172752886],
            ],
            [
                [0.564018699314289, 0.078569916414135],
                [0.973553199990880, 0.478552815466372],
                [0.999309166012882, 0.813620981660388],
            ],
        ]
    )
    assert abs(c_table - s).max() < 1e-9

    assert_raises(ValueError, stats.order_stats, "badwhichoption", p=0.99, c=0.90, r=4)