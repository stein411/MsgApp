export SPEECHSDK_ROOT="text_to_speech"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$SPEECHSDK_ROOT/lib/x64"
./text_to_speech_program
rm lines_to_synth
touch lines_to_synth
