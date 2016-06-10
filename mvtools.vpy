import vapoursynth as vs
core = vs.get_core()
clip = core.ffms2.Source(source="ffv1/24fps/native.mkv")

sup  = core.mv.Super(clip)
bvec = core.mv.Analyse(sup, isb=True)
fvec = core.mv.Analyse(sup, isb=False)
clip = core.mv.FlowFPS(clip, sup, bvec, fvec, num=60)

clip.set_output()
