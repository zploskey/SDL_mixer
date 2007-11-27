# Temporary hack until SDL directly supports pulseaudio
# If alsa-plugins-pulseaudio is installed, force SDL to output sound to esd
set nonomatch
if ( -e /usr/lib*/alsa-lib/libasound_module_pcm_pulse.so ) setenv SDL_AUDIODRIVER esd
