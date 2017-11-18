import os, subprocess, logging
"""
copied from network, 
"""

def amr2mp3(amr_path, mp3_path=None):
    """ convert amr to mp3 just amr file to mp3 file
    """
    path, name = os.path.split(amr_path)
    if name.split('.')[-1] != 'amr':
        print('not a amr file')
        return 0
    if mp3_path is None or mp3_path.split('.')[-1] != 'mp3':
         mp3_path = os.path.join(path, name + '.mp3')
         error = subprocess.call(['ffmpeg', '-i', amr_path, mp3_path])
    if error:
        logging.error('[Convert Error]:Convert file-%s to mp3 failed' % amr_path)
        return 0
    return mp3_path