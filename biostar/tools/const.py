# Datatypes

RADIO = "RADIO"
DROPDOWN = "DROPDOWN"
INTEGER = "INTEGER"
FLOAT = "FLOAT"
UPLOAD = "UPLOAD"
MODEL = "MODEL"
SCRIPT = "SCRIPT"
CHECKBOX = "CHECKBOX"
TEMPLATE = "TEMPLATE"
CHAR = "CHAR"


# Data types
GENERIC_TYPE = 0
SAMPLE_TYPE = 1
COLLECTION_TYPE = 2
TAR_FASTQ_GZ = 3
FASTQ_TYPE = 4
FASTA_TYPE = 5
REFERENCE_TYPE = 6
LAMAR_SAMPLE_SHEET = 7
ACCESSION_MAP =8
TAXONOMY_TYPE = 9

# Data type lookup map.
DATA_TYPES = dict(
    GENERIC_TYPE=GENERIC_TYPE,
    SAMPLE_TYPE=SAMPLE_TYPE,
    COLLECTION_TYPE=SAMPLE_TYPE,
    TAR_FASTQ_GZ=TAR_FASTQ_GZ,
    FASTQ_TYPE=FASTQ_TYPE,
    FASTA_TYPE=FASTA_TYPE,
    REFERENCE_TYPE=REFERENCE_TYPE,
    LAMAR_SAMPLE_SHEET=LAMAR_SAMPLE_SHEET,
    ACCESSION_MAP=ACCESSION_MAP,
    TAXONOMY_TYPE=TAXONOMY_TYPE,
)

# Sequence subtype.
SEQUENCE_TYPES = [FASTA_TYPE, FASTQ_TYPE]
