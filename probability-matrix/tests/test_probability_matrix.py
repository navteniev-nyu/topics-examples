from probability_matrix.main import ProbabilityMatrix

def test_sample() -> None:
    subject = ProbabilityMatrix()

    assert subject.sample() == [0,0]
