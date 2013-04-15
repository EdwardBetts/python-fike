import os
import pickle

class FikeException(Exception):
    pass
    
class Fike:
    def __init__(self, target=None, *args, **kwargs):
        r_fd, w_fd = os.pipe()
        self._child_pid = os.fork()
        if self.is_child():
            # Child process
            os.close(r_fd)
            self._w = os.fdopen(w_fd, 'w')
            ## Now go on and do something, and return the result with
            ## the return_and_die method.

            ## ...Unless the constructor received a target function as
            ## an argument. In that case, execute it immediatelly,
            ## with the given extra arguments if any.
            if target is not None:
                self.return_and_die(target(*args, **kwargs))

        else:
            # Parent process initialization
            os.close(w_fd)
            self._r = os.fdopen(r_fd)
            ## Now go do somethiing else, and then call get_result to
            ## fetch the result from the child process when you will.

    def return_and_die(self, data):
        if self.is_parent():
            raise FikeException("Cannot write to pipe in parent process.")
        self._w.write(pickle.dumps(data))
        self._w.close()
        os._exit(0)

    def get_result(self):
        if self.is_child():
            raise FikeException("Cannot read from pipe in child process.")
        child_result = pickle.loads(self._r.read())
        pid, status = os.waitpid(self._child_pid, 0)
        assert status == 0
        return child_result

    def is_parent(self):
        return not self.is_child()

    def is_child(self):
        return self._child_pid == 0
