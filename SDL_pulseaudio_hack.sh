# Temporary hack until SDL directly supports pulseaudio
# If alsa-plugins-pulseaudio is installed, force SDL to output sound to esd
[ -e /usr/lib*/alsa-lib/libasound_module_pcm_pulse.so ] && export SDL_AUDIODRIVER=esd
