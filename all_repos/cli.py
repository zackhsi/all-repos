import multiprocessing
import sys


def jobs_type(s):
    jobs = int(s)
    if jobs <= 0:
        return multiprocessing.cpu_count()
    else:
        return jobs


def add_jobs_arg(parser, default=8):
    parser.add_argument(
        '-j', '--jobs', type=jobs_type, default=default,
        help=(
            'how many concurrent jobs will be used to complete the '
            'operation.  Specify 0 or -1 to match the number of cpus '
            '(default `%(default)s`).'
        ),
    )


COLOR_CHOICES = ('auto', 'always', 'never')


def use_color(setting):
    if setting not in COLOR_CHOICES:
        raise ValueError(setting)
    return (
        setting == 'always' or
        (setting == 'auto' and sys.stdout.isatty())
    )


def add_common_args(parser):
    parser.add_argument(
        '-C', '--config-filename', default='all-repos.json',
        help='use a non-default config file (default `%(default)s`).',
    )
    parser.add_argument(
        '--color', default='auto', type=use_color,
        metavar='{' + ','.join(COLOR_CHOICES) + '}',
        help='use color in output (default `%(default)s`).',
    )


def add_repos_with_matches_arg(parser):
    parser.add_argument(
        '--repos-with-matches', action='store_true',
        help='only print repositories with matches.',
    )
