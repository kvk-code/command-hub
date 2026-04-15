#!/bin/bash
# Run KTU Tutor View status check
export LD_LIBRARY_PATH=/data/.openclaw/browser-libs
exec python3 "$(dirname "$0")/ktu_tutor_view.py" "$@"
