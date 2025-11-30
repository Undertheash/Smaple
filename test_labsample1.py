import labsample1


def test_get_longest_workout():
   
    
    workouts = labsample1.load_csv()
    assert(
        {
            "date": "25.01.2022",
            "activity": "Cycling",
            "duration": 75.0
        }
    )
    


def test_calc_total_duration():

    workouts = labsample1.load_csv()
    assert(753.0)
    


def test_calc_average_duration():
    workouts = labsample1.load_csv()
    assert(42.65)
