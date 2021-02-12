from maze import Maze
import pytest

@pytest.mark.parametrize('file, goalF',
                         [('maze1.txt',(0, 5)),
                          ('maze2.txt',(8, 13)),
                          ('maze3.txt',(2, 1)),
                          ('maze4.txt',(2, 5)),
                          ('maze5.txt',(29, 62))
                          ])
def test_prueba(file, goalF):
    m = Maze(file)
    m.solve()
    assert m.goal == goalF
