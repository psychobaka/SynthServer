﻿####################################################################################################
# Copyright 2013 John Crawford
#
# This file is part of SynthServer.
#
# SynthServer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SynthServer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SynthServer.  If not, see <http://www.gnu.org/licenses/>.
####################################################################################################

## @file
#  Module Information.
#  @date 3/10/2013 Created file.  -jc
#  @author John Crawford

from engine.mididevice import MIDIVoice



NAME = 'XP-A - SRX-04 - Symphonique Strings'

PATCHES = [
  MIDIVoice('Epic Strings', 93, 3, 0, 'STRINGS', 'XP-A 001'),
  MIDIVoice('sfz! Crsc/sw', 93, 3, 1, 'STRINGS', 'XP-A 002'),
  MIDIVoice('Trem/sw Fine', 93, 3, 2, 'STRINGS', 'XP-A 003'),
  MIDIVoice('Fast Stac/sw', 93, 3, 3, 'STRINGS', 'XP-A 004'),
  MIDIVoice('Str Attack', 93, 3, 4, 'STRINGS', 'XP-A 005'),
  MIDIVoice('Full Pizz mp', 93, 3, 5, 'STRINGS', 'XP-A 006'),
  MIDIVoice('Violins ^/sw', 93, 3, 6, 'STRINGS', 'XP-A 007'),
  MIDIVoice('Violas ^/sw', 93, 3, 7, 'STRINGS', 'XP-A 008'),
  MIDIVoice('Celli ^/sw', 93, 3, 8, 'STRINGS', 'XP-A 009'),
  MIDIVoice('Basses ^/sw', 93, 3, 9, 'STRINGS', 'XP-A 010'),
  MIDIVoice('Fast Section', 93, 3, 10, 'STRINGS', 'XP-A 011'),
  MIDIVoice('F.Str ^/sw', 93, 3, 11, 'STRINGS', 'XP-A 012'),
  MIDIVoice('SymphStrings', 93, 3, 12, 'STRINGS', 'XP-A 013'),
  MIDIVoice('SymphStrngs2', 93, 3, 13, 'STRINGS', 'XP-A 014'),
  MIDIVoice('Vibrato /Aft', 93, 3, 14, 'STRINGS', 'XP-A 015'),
  MIDIVoice('Expressimo', 93, 3, 15, 'STRINGS', 'XP-A 016'),
  MIDIVoice('Spc release', 93, 3, 16, 'STRINGS', 'XP-A 017'),
  MIDIVoice('Hall Strings', 93, 3, 17, 'STRINGS', 'XP-A 018'),
  MIDIVoice('Warm Section', 93, 3, 18, 'STRINGS', 'XP-A 019'),
  MIDIVoice('4Section ^', 93, 3, 19, 'STRINGS', 'XP-A 020'),
  MIDIVoice('4Section Vib', 93, 3, 20, 'STRINGS', 'XP-A 021'),
  MIDIVoice('Sad Strings2', 93, 3, 21, 'STRINGS', 'XP-A 022'),
  MIDIVoice('Pizz&ArcSplt', 93, 3, 22, 'COMBINATION', 'XP-A 023'),
  MIDIVoice('So Swell', 93, 3, 23, 'STRINGS', 'XP-A 024'),
  MIDIVoice('Full Section', 93, 3, 24, 'STRINGS', 'XP-A 025'),
  MIDIVoice('Vibrato /sw', 93, 3, 25, 'STRINGS', 'XP-A 026'),
  MIDIVoice('Octave ^', 93, 3, 26, 'STRINGS', 'XP-A 027'),
  MIDIVoice('Full Sect 2', 93, 3, 27, 'STRINGS', 'XP-A 028'),
  MIDIVoice('Attack Sect', 93, 3, 28, 'STRINGS', 'XP-A 029'),
  MIDIVoice('Velo Strings', 93, 3, 29, 'STRINGS', 'XP-A 030'),
  MIDIVoice('Full Tremolo', 93, 3, 30, 'STRINGS', 'XP-A 031'),
  MIDIVoice('Trem Decresc', 93, 3, 31, 'STRINGS', 'XP-A 032'),
  MIDIVoice('Tension Trem', 93, 3, 32, 'STRINGS', 'XP-A 033'),
  MIDIVoice('F.StrTrm/Mrc', 93, 3, 33, 'STRINGS', 'XP-A 034'),
  MIDIVoice('F.Str Trm/sw', 93, 3, 34, 'STRINGS', 'XP-A 035'),
  MIDIVoice('Trm /Mod&Aft', 93, 3, 35, 'STRINGS', 'XP-A 036'),
  MIDIVoice('F.Str/ModTrm', 93, 3, 36, 'STRINGS', 'XP-A 037'),
  MIDIVoice('Spc Marc /sw', 93, 3, 37, 'STRINGS', 'XP-A 038'),
  MIDIVoice('WarmStaccSec', 93, 3, 38, 'STRINGS', 'XP-A 039'),
  MIDIVoice('StackNirvana', 93, 3, 39, 'STRINGS', 'XP-A 040'),
  MIDIVoice('Spc Sect.8va', 93, 3, 40, 'STRINGS', 'XP-A 041'),
  MIDIVoice('Spc-Mrc /sw', 93, 3, 41, 'STRINGS', 'XP-A 042'),
  MIDIVoice('Mrc-Spc /sw', 93, 3, 42, 'STRINGS', 'XP-A 043'),
  MIDIVoice('Full Spc /sw', 93, 3, 43, 'STRINGS', 'XP-A 044'),
  MIDIVoice('Marc & Pizz', 93, 3, 44, 'STRINGS', 'XP-A 045'),
  MIDIVoice('PizzL+SpiccR', 93, 3, 45, 'STRINGS', 'XP-A 046'),
  MIDIVoice('Pizz Sect', 93, 3, 46, 'STRINGS', 'XP-A 047'),
  MIDIVoice('Full Pizz pp', 93, 3, 47, 'STRINGS', 'XP-A 048'),
  MIDIVoice('Full Pizz ff', 93, 3, 48, 'STRINGS', 'XP-A 049'),
  MIDIVoice('4Sect. Pz ff', 93, 3, 49, 'STRINGS', 'XP-A 050'),
  MIDIVoice('Double Pizz', 93, 3, 50, 'STRINGS', 'XP-A 051'),
  MIDIVoice('sfz! Vln /sw', 93, 3, 51, 'STRINGS', 'XP-A 052'),
  MIDIVoice('Violin Sect1', 93, 3, 52, 'STRINGS', 'XP-A 053'),
  MIDIVoice('Violin Sect2', 93, 3, 53, 'STRINGS', 'XP-A 054'),
  MIDIVoice('Violin Sect3', 93, 3, 54, 'STRINGS', 'XP-A 055'),
  MIDIVoice('Warm Vln Sec', 93, 3, 55, 'STRINGS', 'XP-A 056'),
  MIDIVoice('GrandVln&Vcs', 93, 3, 56, 'STRINGS', 'XP-A 057'),
  MIDIVoice('Vln Sect mp', 93, 3, 57, 'STRINGS', 'XP-A 058'),
  MIDIVoice('Slow Atk Vln', 93, 3, 58, 'STRINGS', 'XP-A 059'),
  MIDIVoice('Vln/Mod Pizz', 93, 3, 59, 'STRINGS', 'XP-A 060'),
  MIDIVoice('Vln Stc/Mrc', 93, 3, 60, 'STRINGS', 'XP-A 061'),
  MIDIVoice('Vn Piz/Spcff', 93, 3, 61, 'STRINGS', 'XP-A 062'),
  MIDIVoice('Vln Marcato', 93, 3, 62, 'STRINGS', 'XP-A 063'),
  MIDIVoice('Vln Pizz /sw', 93, 3, 63, 'STRINGS', 'XP-A 064'),
  MIDIVoice('sfz! Va /sw', 93, 3, 64, 'STRINGS', 'XP-A 065'),
  MIDIVoice('Viola Sect 1', 93, 3, 65, 'STRINGS', 'XP-A 066'),
  MIDIVoice('Viola Sect 2', 93, 3, 66, 'STRINGS', 'XP-A 067'),
  MIDIVoice('Va Stc/Mrc', 93, 3, 67, 'STRINGS', 'XP-A 068'),
  MIDIVoice('Va /Mod Pizz', 93, 3, 68, 'STRINGS', 'XP-A 069'),
  MIDIVoice('Va Marcato', 93, 3, 69, 'STRINGS', 'XP-A 070'),
  MIDIVoice('Va Pizz /sw', 93, 3, 70, 'STRINGS', 'XP-A 071'),
  MIDIVoice('sfz! Vc /sw', 93, 3, 71, 'STRINGS', 'XP-A 072'),
  MIDIVoice('Cello Sect 1', 93, 3, 72, 'STRINGS', 'XP-A 073'),
  MIDIVoice('Cello Sect 2', 93, 3, 73, 'STRINGS', 'XP-A 074'),
  MIDIVoice('Warm Vc Sect', 93, 3, 74, 'STRINGS', 'XP-A 075'),
  MIDIVoice('Vc Pizz /sw', 93, 3, 75, 'STRINGS', 'XP-A 076'),
  MIDIVoice('Vc /Mod Pizz', 93, 3, 76, 'STRINGS', 'XP-A 077'),
  MIDIVoice('Vc Marcato', 93, 3, 77, 'STRINGS', 'XP-A 078'),
  MIDIVoice('Vc Stc/Mrc', 93, 3, 78, 'STRINGS', 'XP-A 079'),
  MIDIVoice('Vc Piz/Spcff', 93, 3, 79, 'STRINGS', 'XP-A 080'),
  MIDIVoice('sfz! Cb /sw', 93, 3, 80, 'STRINGS', 'XP-A 081'),
  MIDIVoice('Cb /Mod Pizz', 93, 3, 81, 'STRINGS', 'XP-A 082'),
  MIDIVoice('Bass Sect 1', 93, 3, 82, 'STRINGS', 'XP-A 083'),
  MIDIVoice('Cbs Marcato', 93, 3, 83, 'STRINGS', 'XP-A 084'),
  MIDIVoice('Cbs Stc/Mrc', 93, 3, 84, 'STRINGS', 'XP-A 085'),
  MIDIVoice('Cbs Pizz /sw', 93, 3, 85, 'STRINGS', 'XP-A 086'),
  MIDIVoice('Symphonique2', 93, 3, 86, 'ORCHESTRA', 'XP-A 087'),
  MIDIVoice('Soundtrk Str', 93, 3, 87, 'STRINGS', 'XP-A 088'),
  MIDIVoice('LargeStrings', 93, 3, 88, 'STRINGS', 'XP-A 089'),
  MIDIVoice('Slow Atk Str', 93, 3, 89, 'STRINGS', 'XP-A 090'),
  MIDIVoice('LushStrings2', 93, 3, 90, 'STRINGS', 'XP-A 091'),
  MIDIVoice('Pop Strings', 93, 3, 91, 'STRINGS', 'XP-A 092'),
  MIDIVoice('102 Violins', 93, 3, 92, 'STRINGS', 'XP-A 093'),
  MIDIVoice('MultiStakato', 93, 3, 93, 'STRINGS', 'XP-A 094'),
  MIDIVoice('Spicatto Arp', 93, 3, 94, 'STRINGS', 'XP-A 095'),
  MIDIVoice('Dim. Pizz', 93, 3, 95, 'STRINGS', 'XP-A 096'),
  MIDIVoice('RhythmicPizz', 93, 3, 96, 'STRINGS', 'XP-A 097'),
  MIDIVoice('Harp StrPad', 93, 3, 97, 'COMBINATION', 'XP-A 098'),
  MIDIVoice('Trem-Guitar', 93, 3, 98, 'AC.GUITAR', 'XP-A 099'),
  MIDIVoice('Baroque Ens2', 93, 3, 99, 'COMBINATION', 'XP-A 100'),
  MIDIVoice('ImitatEP Pad', 93, 3, 100, 'OTHER SYNTH', 'XP-A 101'),
  MIDIVoice('Daybreak Ens', 93, 3, 101, 'OTHER SYNTH', 'XP-A 102'),
  MIDIVoice('Grand Unison', 93, 3, 102, 'ORCHESTRA', 'XP-A 103'),
  MIDIVoice('Va Sect&Glkn', 93, 3, 103, 'ORCHESTRA', 'XP-A 104'),
  MIDIVoice('SRX Symphony', 93, 3, 104, 'ORCHESTRA', 'XP-A 105'),
  MIDIVoice('XV Orchestra', 93, 3, 105, 'ORCHESTRA', 'XP-A 106'),
  MIDIVoice('Full Orch 1', 93, 3, 106, 'ORCHESTRA', 'XP-A 107'),
  MIDIVoice('Orc with Str', 93, 3, 107, 'ORCHESTRA', 'XP-A 108'),
  MIDIVoice('Symphnic Orc', 93, 3, 108, 'ORCHESTRA', 'XP-A 109'),
  MIDIVoice('Strings&Hrns', 93, 3, 109, 'ORCHESTRA', 'XP-A 110'),
  MIDIVoice('Strgs&Hrns 2', 93, 3, 110, 'ORCHESTRA', 'XP-A 111'),
  MIDIVoice('Octa StrEns', 93, 3, 111, 'BRIGHT PAD', 'XP-A 112'),
  MIDIVoice('Antique Str', 93, 3, 112, 'SOFT PAD', 'XP-A 113'),
  MIDIVoice('SweepSectStr', 93, 3, 113, 'SOFT PAD', 'XP-A 114'),
  MIDIVoice('Stereo Tron!', 93, 3, 114, 'STRINGS', 'XP-A 115'),
  MIDIVoice('Horror Str.', 93, 3, 115, 'STRINGS', 'XP-A 116'),
  MIDIVoice('DanzSurround', 93, 3, 116, 'STRINGS', 'XP-A 117'),
  MIDIVoice('Ether Strngs', 93, 3, 117, 'SOFT PAD', 'XP-A 118'),
  MIDIVoice('MoveFX Str', 93, 3, 118, 'SYNTH FX', 'XP-A 119'),
  MIDIVoice('Phase /Aft', 93, 3, 119, 'BRIGHT PAD', 'XP-A 120'),
  MIDIVoice('PhazeStrngs2', 93, 3, 120, 'BRIGHT PAD', 'XP-A 121'),
  MIDIVoice('Reverse Str2', 93, 3, 121, 'STRINGS', 'XP-A 122'),
  MIDIVoice('Haunted', 93, 3, 122, 'SYNTH FX', 'XP-A 123'),
  MIDIVoice('Rewind Vln', 93, 3, 123, 'BRIGHT PAD', 'XP-A 124'),
  MIDIVoice('Synthy Sweep', 93, 3, 124, 'SYNTH FX', 'XP-A 125'),
  MIDIVoice('Ripple', 93, 3, 125, 'SYNTH FX', 'XP-A 126'),
  MIDIVoice('Mystery 2', 93, 3, 126, 'BRIGHT PAD', 'XP-A 127'),
  MIDIVoice('Rising STR', 93, 3, 127, 'SYNTH FX', 'XP-A 128'),
]