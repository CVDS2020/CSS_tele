include $(top_srcdir)/build/modmake.rulesam
MODNAME=mod_say_en

mod_LTLIBRARIES = mod_say_en.la
mod_say_en_la_SOURCES  = mod_say_en.c
mod_say_en_la_CFLAGS   = $(AM_CFLAGS)
mod_say_en_la_LIBADD   = $(switch_builddir)/libfreeswitch.la
mod_say_en_la_LDFLAGS  = -avoid-version -module -no-undefined -shared
