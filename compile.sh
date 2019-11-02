#apt-get install build-essential libssl1.0.0 libasound2 wget
export SPEECHSDK_ROOT="text_to_speech"

# compile the program
g++ helloworld.cpp -o text_to_speech_program -I "$SPEECHSDK_ROOT/include/cxx_api" -I "$SPEECHSDK_ROOT/include/c_api" --std=c++14 -lpthread -lMicrosoft.CognitiveServices.Speech.core -L "$SPEECHSDK_ROOT/lib/x64" -l:libasound.so.2
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$SPEECHSDK_ROOT/lib/x64"
