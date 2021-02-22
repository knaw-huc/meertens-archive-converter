# encoding: utf-8
import logging
# from logging.handlers import RotatingFileHandler
import shutil
from logging import handlers
import sys
import os
import errno

""" configuration """
db_host = 'db'
db_name = 'mydb'
db_user = 'root'
db_pass = 'root'
ROOT = '/data2/DigitaleOnderzoekscollecties'
DUMMYLOCATION = '/data2/DigitaleOnderzoekscollecties-precollection'
LOGFILE = 'logfile'

""" init log and format """
log = logging.getLogger('')
log.setLevel(logging.DEBUG)
log_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

""" log to standard out """
ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(log_format)
log.addHandler(ch)

""" log to file """
fh = handlers.RotatingFileHandler(LOGFILE, maxBytes=(1048576 * 50), backupCount=7)
fh.setFormatter(log_format)
log.addHandler(fh)


def disk_files(path):
    """ put all files from disk into a set generator """
    log.info('### Getting all files from disk to set ###')
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            yield os.path.join(dirpath, filename)


def get_file_components(full_filename):
    filename = os.path.basename(full_filename)
    _, extension = os.path.splitext(full_filename)
    full_path = os.path.dirname(full_filename)
    return full_path, filename, extension


def load_ext_from_code():
    rows = {'ha': 'OK', 'rtf': 'OK', '_anko': 'Verwijderen', 'aiff': '.aif', 'gz': 'OK', 'jpeg': 'OK', 'mp4': 'OK',
            'mp3': 'OK', 'itx': 'OK', '_pauwels_1958_002-268': 'Verwijderen', 'ttf': 'OK', 'xml': 'OK', 'cut': 'OK',
            'weg': 'OK', '_wld-part-iii': 'Verwijderen', '7tif': '.tif', 'wmv': 'OK',
            'dvdproj/contents/resources/projectdata': '.xml', 'htmvvvv': '.html', '_wbd': 'Verwijderen', 'wma': 'OK',
            'm4a': 'OK', 'ly': 'OK', 'bin': 'OK', 'mpg': 'OK', 'docx': 'OK', 'nvp': 'OK', '_tntl': 'Verwijderen',
            'woff': 'OK', 'db': 'OK', 'mov': 'OK', '_onze_taal': 'Verwijderen', 'pfsx': 'OK', 'dat': 'OK',
            'htm~~': '.html', 'fmp12': 'OK', '_wld': 'Verwijderen', 'part': '.pdf', 'amr': 'OK', 'mrg': 'OK',
            'pst': 'OK', 'mod': 'OK', 'hqx': 'OK', '_kloeke_ongepubliceerd': 'Verwijderen', 'eml': 'OK',
            '_spreafico_2013': 'Verwijderen', '_mi_ongepubliceerd': 'Verwijderen', 'lst': 'OK', '_and': 'Verwijderen',
            'dwl': 'OK', 'xsd': 'OK', '_lomelle': 'Verwijderen', 'ifo': 'OK', '_weijnen_1987': 'Verwijderen',
            'bak': 'OK', '_nedt_aanv': 'Verwijderen', 'ek': 'OK', 'mdb': 'OK', '_db': 'Verwijderen', 'ppt': 'OK',
            'odt': 'OK', ' 2002': '.pdf', 'lnk': 'OK', '_wld-part-i': 'Verwijderen', 'tmp': 'OK',
            '_hctd': 'Verwijderen', '_wbd-part-iii': 'Verwijderen', '_ntg': 'Verwijderen',
            '_volkskunde_atlas': 'Verwijderen', '_vginneken2': 'Verwijderen', 'cha': 'OK',
            '_wgd-rivierengebied': 'Verwijderen', '~152b1ef': 'Verwijderen', 'pek': 'OK', 'orig': '.csv', 'hh': 'OK',
            '_vldn': 'Verwijderen', 'bc': 'OK', 'js': 'OK', 'prproj': 'OK', '_ott': 'Verwijderen',
            '_goossens_1988': 'Verwijderen', '6tif': '.tif', '_tnzn': 'Verwijderen', '_mncdn': 'Verwijderen',
            '_goossens_1981': 'Verwijderen', 'xls': 'OK', '_weijnen_2009': 'Verwijderen',
            '_hout_van_ea_1996': 'Verwijderen', 'krn': 'OK', 'pdf': 'OK', '_sijs_van_der_2014': 'Verwijderen',
            'tgz': 'OK', 'tiff': '.tif', 'sql': 'OK', 'owa': 'OK', '_dialectatlas_2011': 'Verwijderen',
            '_ton': 'Verwijderen', '_eigen_volk_aanv': 'Verwijderen', 'raw': 'OK', '5tif': '.tif', 'txt': 'OK',
            '_weijnen_1977': 'Verwijderen', '_pee_1936_aanv': 'Verwijderen', '_kruijsen_1995': 'Verwijderen',
            '_wbd-part-ii': 'Verwijderen', 'jp2': 'OK', 'log': 'OK', 'zip': 'OK', '_wld-part-ii': 'Verwijderen',
            'swf': 'OK', 'gif': 'OK', 'json': 'OK', '_tabu': 'Verwijderen', 'wav': 'OK', 'htm': 'OK', 'xlsx': 'OK',
            'eaf': 'OK', '_veldeke_aanv': 'Verwijderen', 'bup': 'OK', '_lamelli_2010': 'Verwijderen', '2tif': '.tif',
            'bmp': 'OK', "/1049:1_depot_afbeeldingen/groepsfoto's meertens instituut/groepsfoto": '.tif', 'cmdi': 'OK',
            '_bin': 'Verwijderen', 'pk': 'OK', '_cajot_1979': 'Verwijderen', '_roerstreek': 'Verwijderen', 'xlsb': 'OK',
            'png': 'OK', 'rss': 'OK', 'info': 'OK', '_franse_ned': 'Verwijderen', '_wbd-part-i': 'Verwijderen',
            '3tif': '.tif', 'mts': 'OK', '_sand': 'Verwijderen', '_weijnen_1952': 'Verwijderen', 'flv': 'OK',
            'htaccess': 'OK', '1tif': '.tif', 'svg': 'OK', '_kruijsen_2006': 'Verwijderen', 'utx': 'OK', 'aif': '.aif',
            'ini': 'Verwijderen', '_brok_2006': 'Verwijderen', '_spektator': 'Verwijderen',
            '_berteloot_1984': 'Verwijderen', 'vob': 'OK', '_vginneken1': 'Verwijderen', 'ak': 'OK',
            '_atlas_peters': 'Verwijderen', 'spt': 'OK', 'jpg': 'OK', 'textgrid': 'OK', '_lb_aanv': 'Verwijderen',
            'avi': 'OK', 'tab': 'OK', 'wks': 'OK', '_rem_2003': 'Verwijderen', 'plist': 'OK', 'imdi': 'OK',
            'htm~': '.html', 'ef': 'OK', 'wpk': 'OK', 'cha~': '.cha', 'mid': 'OK',
            ') 01: 1983 - 1984/dagboek 1983 inleiding': 'Verwijderen', 'sav': 'OK', 'html': 'OK', 'wce': 'OK',
            '_naamkunde': 'Verwijderen', 'tif': 'OK', 'csv': 'OK', 'css': 'OK', 'php3': 'OK', 'ds_store': 'Verwijderen',
            'bks': 'OK', '_wgd-veluwe': 'Verwijderen', 'class': 'OK', 'tbt': 'OK', '4tif': '.tif', '001': '.eaf',
            'mpeg': 'OK', 'psd': 'OK', '_mand': 'Verwijderen', '_tent_aanv': 'Verwijderen', 'wpd': 'OK', 'php': 'OK',
            '_tnf': 'Verwijderen', 'm4v': 'OK', 'exe': 'OK', 'doc': 'OK', 'imdi~': '.imdi', 'eps': 'OK', 'jbf': 'OK',
            'fp7': 'OK', 'sh': 'OK', 'dos': 'OK', '_fand': 'Verwijderen', 'cpt': 'OK', 'dot': 'OK', 'testtest': 'Verwijderen'}
    return rows


def load_ext_from_db():
    """
    Load all dist(ext, waard) in one goal
    :return: rows: dict(ext, waard)
    """
    try:
        """ init db """
        import MySQLdb
        db = MySQLdb.connect(host=db_host,
                             user=db_user,
                             passwd=db_pass,
                             db=db_name)
        cur = db.cursor()
    except:
        log.error('No db connector available! Try loading exts from code!')
        return None

    sql = 'select ext, waarde from stoplijst;'
    cur.execute(sql)
    rows = dict()

    for row in cur.fetchall():
        rows[str.lower(row[0])] = row[1]

    return rows


def get_waarde(ext):
    """
    get waarde using ext as key
    :param ext: string
    :return: waard: string
    """
    global exts
    waarde = ''
    try:
        waarde = exts[ext.strip().lower()]
        # waarde = exts[str.lower(str.strip(ext))]
    except:
        pass
    return waarde


def move_to_dummy_folder(full_filename, new_location_postfix=DUMMYLOCATION):
    global dryrun
    new_location = full_filename.replace(ROOT, new_location_postfix)
    new_full_path, _, _ = get_file_components(new_location)

    if dryrun:
        if os.path.isfile(full_filename):
            log.debug('Dryrun - \nold location is: [%s]\nnew location is: [%s]' % (full_filename, new_location))
        else:
            log.error('Dryrun - \nold location is: [%s]\nnew location is: [%s]; [%s]' % (full_filename, new_location))
    else:
        folder_ok = True
        try:
            os.makedirs(new_full_path)
        except OSError, e:
            if e.errno != errno.EEXIST:
                log.error('Cannot create folder: [%s]; for file [%s]' % (new_full_path, full_filename))
                folder_ok = False

        if folder_ok:
            try:
                # use copy2 and unlink instead of move
                # This makes sure that the metadata of the file gets preserved
                shutil.copy2(full_filename, new_location)
                os.unlink(full_filename)
                log.info('Moving - \nold location is: [%s]\nnew location is: [%s]' % (full_filename, new_location))
            except Exception, e:
                print('%s' % e)
                print('%s' % e.message)
                log.error('File [%s] failed to move to [%s]; original error message: [%s]' % (full_filename, new_location, e.message))


def append_waarde_to_file_name(full_filename, waarde):
    global dryrun
    newname = full_filename + waarde

    if dryrun:
        log.debug('Dryrun - \nold name is: [%s]\nnew name is: [%s]' % (full_filename, newname))
    else:
        try:
            # use copy2 and unlink instead of os.rename
            # This makes sure that the metadata of the file gets preserved
            shutil.copy2(full_filename, newname)
            os.unlink(full_filename)
            log.info('Renaming - \nold name is: [%s]\nnew name is: [%s]' % (full_filename, newname))
        except Exception as e:
            log.error('File [%s] failed to rename to [%s]; original error message: [%s]' % (full_filename, newname, e.message))


def clean_files(disk_file_set):
    log.info('### START PROCESSING FILES ###')

    counter = 0
    for full_filename in disk_file_set:
        counter += 1
        # log.info('### Processing [%s] ###' % full_filename)
        full_path, filename, extension = get_file_components(full_filename)
        if extension is not '':
            extension = extension[1:] if extension[0] == '.' else extension

            waarde = get_waarde(extension)
            # log.debug('%s-%s' % (counter, waarde))
            if waarde == 'Verwijderen':
                # mv the file to dummy folder
                move_to_dummy_folder(full_filename)
            elif waarde == 'OK':
                pass
            elif waarde == '':
                log.error('File [%s] has invalid extension [%s] or waarde is empty string' %
                          (full_filename, extension.strip().lower()))
            else:
                # append waarde to filename
                append_waarde_to_file_name(full_filename, waarde)
        else:
            log.error('File [%s] has no extension' % full_filename)
            continue
        # print('full path: [%s]; filename: [%s]; ext: [%s]' % (full_path, filename, extension))

    log.info('### FINISH PROCESSING [%s] FILES ###' % counter)


if __name__ == '__main__':
    dryrun = False
    exts = ''

    while True:
        print('###########################')
        print('lc for load exts from code')
        print('l for load exts from db')
        print('e for print exts')
        print("d for dry-run")
        print("r for run")
        print("q to quit")
        print('###########################')
        command = raw_input('Choose command: ')
        print("you choose: [%s]" % command)

        if command == 'd':
            dryrun = True
            if exts == '':
                print('### ERROR: Please load exts first ###\n\n')
                continue
            disk_file_set = disk_files(ROOT)
            clean_files(disk_file_set)
            pass
        elif command == 'r':
            dryrun = False
            if exts == '':
                print('### ERROR: Please load exts first ###\n\n')
                continue
            disk_file_set = disk_files(ROOT)
            clean_files(disk_file_set)
        elif command == 'lc':
            log.info('### Loading extension from code ###')
            exts = load_ext_from_code()
        elif command == 'l':
            log.info('### Loading extension from db ###')
            exts = load_ext_from_db()
        elif command == 'q':
            break
        elif command == 'e':
            print('size is: [%s]; [%s]' % (len(exts), exts))
        else:
            pass
