__all__ = ['BadSignalWarning']

class BadSignalWarning(UserWarning):
    '''
    Warning class to raise when no heart rate is detectable in supplied signal.
    
    This warning notifies the user that the supplied signal is of insufficient quality and/or does not contain enough information to properly process.
    '''
