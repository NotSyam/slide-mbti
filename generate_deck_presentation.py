# -*- coding: utf-8 -*-
"""
Revised Generator for 'Building Team Using Personality Perspective'
- Full HD 1920x1080 Bento Grid Layout with Maximum Negative Space
- Floating / Non-obtrusive glass navigation pill (no bottom bar eating up space)
- Square Box with PT. PP Logo in Top-Left across all slides
- Portrait Photos with Linear Gradient Mask:
  * Head & face are clear, distinct, and visible (high opacity)
  * Body blends seamlessly into white background
- Bullet lists with exact mathematical alignment between icons and text lines
- Strict professional Bahasa Indonesia
- Large, high-contrast typography for 45+ audience
"""

import os
import json
import base64

output_file = r"D:\Abdullah Syamsidar\Campur Aduk (AGY)\personality_perspective_presentation.html"
assets_dir = r"D:\Abdullah Syamsidar\Campur Aduk (AGY)\tokoh_assets"
logo_path = r"C:\Users\fariz\.gemini\antigravity\brain\293e051e-2eef-4e59-9886-9c0c62dbd90a\.user_uploaded\media_1790665817547.png"

# Load Logo
with open(logo_path, "rb") as f:
    logo_b64 = f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

# Load and encode images to base64
def get_b64_image(filename):
    path = os.path.join(assets_dir, filename)
    if os.path.exists(path):
        mime = "image/webp" if filename.lower().endswith(".webp") else "image/png" if filename.lower().endswith(".png") else "image/jpeg"
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
            return f"data:{mime};base64,{data}"
    return ""

img_ahok = get_b64_image("page_16_0_Image1952.jpg")
img_dahlan = get_b64_image("page_17_0_Image1998.jpg")
img_maudy = get_b64_image("page_18_0_Image2043.jpg")
img_maia = get_b64_image("page_19_0_Image2083.jpg")
img_habibie = get_b64_image("page_20_0_Image2123.jpg")
img_tony = get_b64_image("page_21_0_Image2149.jpg")
img_gusdur = get_b64_image("page_22_0_Image2189.jpg")
img_srimulyani = get_b64_image("page_23_0_Image2215.jpg")
img_sandiaga = get_b64_image("page_24_0_Image2255.jpg")
img_enzy = get_b64_image("page_25_0_Image2295.jpg")
img_najwa = get_b64_image("page_26_0_Image2335.jpg")
img_iwan = get_b64_image("page_27_0_Image2375.jpg")
img_deddy = get_b64_image("page_28_0_Image2401.webp")
img_raffi = get_b64_image("page_29_0_Image2441.jpg")
img_ahy = get_b64_image("page_30_0_Image2481.jpg")
img_jobs = get_b64_image("page_31_0_Image2521.jpg")

# Reusable header component with PT. PP square logo in top-left
def make_header(category, title, badge_text, badge_color="bg-[#4F90F6]/15 text-[#1D4ED8] border-[#4F90F6]/30"):
    return f"""
    <div class="flex items-center justify-between pb-4 border-b-2 border-slate-200/90 mb-6">
        <div class="flex items-center gap-5">
            <!-- Kotak Persegi Logo PT. PP -->
            <div class="w-16 h-16 rounded-2xl bg-white border-2 border-slate-200 shadow-sm flex items-center justify-center p-2.5 flex-shrink-0">
                <img src="{logo_b64}" class="w-full h-full object-contain" alt="PT. PP Logo" />
            </div>
            <div>
                <div class="flex items-center gap-2 text-[#2563EB] font-extrabold text-xs uppercase tracking-widest mb-1">
                    <span class="material-symbols-outlined text-base">corporate_fare</span>
                    {category}
                </div>
                <h2 class="text-3xl font-black text-[#0D1B2A] tracking-tight">{title}</h2>
            </div>
        </div>
        <div class="px-5 py-2 rounded-full {badge_color} font-black text-sm border shadow-sm flex items-center gap-2">
            <span class="material-symbols-outlined text-lg">verified</span>
            {badge_text}
        </div>
    </div>
    """

# Archetype card with Top Header (MBTI + The... + Name), Middle Photo Window, and Bottom Text Cards
def make_archetype_card(type_code, type_title, figure_name, img_data, strengths, weaknesses, partner_types, badge_bg="bg-[#2563EB]"):
    s_html = "".join([
        f"""<li class="bento-bullet">
            <span class="bullet-icon text-emerald-600"><span class="material-symbols-outlined text-[20px]">check_circle</span></span>
            <span class="bullet-text text-sm font-bold text-[#0D1B2A]">{s}</span>
        </li>""" for s in strengths
    ])
    w_html = "".join([
        f"""<li class="bento-bullet">
            <span class="bullet-icon text-rose-600"><span class="material-symbols-outlined text-[20px]">warning</span></span>
            <span class="bullet-text text-sm font-semibold text-[#475569]">{w}</span>
        </li>""" for w in weaknesses
    ])
    
    return f"""
    <div class="relative bg-white rounded-[28px] border-2 border-slate-200 shadow-md p-5 flex flex-col justify-between overflow-hidden group hover:border-[#2563EB] transition-all">
        <!-- Photo with Linear Gradient Mask: Head & Face are prominently visible below top header, torso fades into white -->
        <div class="absolute top-[76px] left-0 right-0 h-[50%] pointer-events-none overflow-hidden select-none"
             style="-webkit-mask-image: linear-gradient(to bottom, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.90) 52%, rgba(0,0,0,0.2) 82%, rgba(0,0,0,0) 100%); mask-image: linear-gradient(to bottom, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.90) 52%, rgba(0,0,0,0.2) 82%, rgba(0,0,0,0) 100%);">
            <img src="{img_data}" class="w-full h-full object-cover object-top filter grayscale-[10%] contrast-115 opacity-85 transition-transform duration-500 group-hover:scale-105" alt="{figure_name}" />
        </div>

        <!-- Foreground Content (z-10 ensures 100% crisp readability) -->
        <div class="relative z-10 flex flex-col justify-between h-full">
            <!-- 1. TOP HEADER CARD: MBTI Code, Archetype Title ('The...'), dan Nama Tokoh tetap di bagian ATAS -->
            <div class="bg-white/95 backdrop-blur-md border border-slate-200/90 rounded-2xl p-3 shadow-sm mb-2 flex-shrink-0">
                <div class="flex items-center justify-between mb-1">
                    <span class="px-2.5 py-0.5 rounded-lg {badge_bg} text-white font-black text-xs tracking-wide shadow-sm">{type_code}</span>
                    <span class="text-[11px] font-extrabold text-[#475569] uppercase tracking-wider">{type_title}</span>
                </div>
                <div class="text-xl font-black text-[#0D1B2A] tracking-tight truncate">
                    {figure_name}
                </div>
            </div>

            <!-- 2. OPEN PHOTO WINDOW: Ruang terbuka khusus agar kepala & wajah tokoh terlihat jelas tanpa terhalang text card -->
            <div class="h-[185px] w-full flex-shrink-0"></div>

            <!-- 3. BOTTOM SECTION: Text Cards untuk Kekuatan, Titik Buta, dan Mitra Ideal digeser ke BAWAH -->
            <div class="flex-1 flex flex-col justify-between">
                <!-- Strengths (+) with pure contrast background -->
                <div class="mb-2.5 bg-white/90 backdrop-blur-[2px] rounded-2xl p-2.5 border border-slate-100/90 shadow-xs">
                    <div class="text-xs font-black text-emerald-800 uppercase tracking-wider mb-1.5 flex items-center gap-1.5">
                        <span class="material-symbols-outlined text-base">verified</span> KEKUATAN ALAMI (+)
                    </div>
                    <ul class="space-y-1.5">
                        {s_html}
                    </ul>
                </div>

                <!-- Blindspots (-) -->
                <div class="mb-2.5 bg-white/90 backdrop-blur-[2px] rounded-2xl p-2.5 border border-slate-100/90 shadow-xs">
                    <div class="text-xs font-black text-rose-800 uppercase tracking-wider mb-1.5 flex items-center gap-1.5">
                        <span class="material-symbols-outlined text-base">report_problem</span> TITIK BUTA / WASPADA (-)
                    </div>
                    <ul class="space-y-1.5">
                        {w_html}
                    </ul>
                </div>

                <!-- Footer Mitra Sinergi -->
                <div class="pt-2 border-t border-slate-200/90 text-xs font-bold text-[#334155] flex items-center justify-center gap-1.5 bg-slate-50/90 rounded-xl py-2 px-3">
                    <span>🤝 Mitra Ideal:</span>
                    <span class="text-[#2563EB] font-black">{partner_types}</span>
                </div>
            </div>
        </div>
    </div>
    """

slides = [
    # SLIDE 1: COVER
    {
        "id": 1,
        "category": "PEMBUKA",
        "title": "Membangun Tim Melalui Perspektif Kepribadian",
        "html": f"""
        <div class="h-full grid grid-cols-12 gap-8">
            <!-- Left Hero Card (8 cols) -->
            <div class="col-span-8 bg-gradient-to-br from-white via-[#F8FAFC] to-[#EBF3FE] p-16 rounded-[36px] border-2 border-[#4F90F6]/30 shadow-2xl flex flex-col justify-between relative overflow-hidden">
                <div class="absolute -right-20 -bottom-20 w-96 h-96 rounded-full bg-[#4F90F6]/15 blur-3xl pointer-events-none"></div>
                
                <div>
                    <!-- Top Bar with PT. PP Square Box Logo -->
                    <div class="flex items-center gap-4 mb-8">
                        <div class="w-16 h-16 rounded-2xl bg-white border-2 border-slate-200 shadow-md flex items-center justify-center p-2.5 flex-shrink-0">
                            <img src="{logo_b64}" class="w-full h-full object-contain" alt="PT. PP Logo" />
                        </div>
                        <div class="inline-flex items-center gap-2.5 px-5 py-2.5 rounded-full bg-[#4F90F6]/15 border border-[#4F90F6]/35 text-[#1D4ED8] font-black text-sm tracking-wider uppercase shadow-sm">
                            <span class="material-symbols-outlined text-xl">diversity_3</span>
                            DAPENDA EXECUTIVE GATHERING • 2024
                        </div>
                    </div>

                    <h1 class="text-6xl font-black text-[#0D1B2A] tracking-tight leading-[1.12] mb-6">
                        MEMBANGUN TIM DENGAN <br/>
                        <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#2563EB] via-[#4F90F6] to-[#0284C7]">PERSPEKTIF KEPRIBADIAN</span>
                    </h1>
                    <p class="text-2xl text-[#334155] font-semibold leading-relaxed max-w-3xl">
                        Mengenali Potensi Diri dan Karakter Rekan Kerja: Panduan terstruktur mengelola keberagaman kognitif demi terciptanya sinergi tim yang produktif dan harmonis.
                    </p>
                </div>
                
                <div class="pt-8 border-t-2 border-slate-200 flex items-center justify-between text-[#475569] text-lg font-bold">
                    <div class="flex items-center gap-8">
                        <span class="flex items-center gap-2.5">
                            <span class="material-symbols-outlined text-[#2563EB] text-2xl">calendar_today</span>
                            27 September 2024
                        </span>
                        <span class="flex items-center gap-2.5">
                            <span class="material-symbols-outlined text-[#2563EB] text-2xl">location_on</span>
                            Auditorium Utama Dapenda
                        </span>
                    </div>
                    <span class="flex items-center gap-2.5 text-[#0D1B2A]">
                        <span class="material-symbols-outlined text-[#2563EB] text-2xl">verified</span>
                        People & Culture Leadership Series
                    </span>
                </div>
            </div>

            <!-- Right Column Bento (4 cols) -->
            <div class="col-span-4 grid grid-rows-2 gap-8">
                <!-- Top Right Card: Clear Stream Hero -->
                <div class="bg-gradient-to-br from-[#4F90F6] via-[#2B76E5] to-[#1E5BBB] p-10 rounded-[36px] text-white shadow-2xl flex flex-col justify-between relative overflow-hidden">
                    <div class="w-16 h-16 rounded-2xl bg-white/20 backdrop-blur-md flex items-center justify-center mb-4">
                        <span class="material-symbols-outlined text-4xl">psychology</span>
                    </div>
                    <div>
                        <div class="text-5xl font-black mb-3 tracking-tight">16 Tipologi</div>
                        <div class="text-white/95 font-medium text-xl leading-relaxed">
                            Framework psikologi Carl Jung dan Myers-Briggs yang disederhanakan untuk kebutuhan para pemimpin kerja.
                        </div>
                    </div>
                    <div class="pt-4 border-t border-white/25 flex items-center gap-2.5 text-white text-base font-bold">
                        <span class="material-symbols-outlined text-xl">check_circle</span>
                        Mengenal Diri Secara Objektif
                    </div>
                </div>

                <!-- Bottom Right Card: Misty Sky Secondary -->
                <div class="bg-gradient-to-br from-[#D9E8FC] via-[#B8D5FA] to-[#9FBEED] p-10 rounded-[36px] text-[#0D1B2A] shadow-xl flex flex-col justify-between border-2 border-[#9FBEED]">
                    <div class="w-16 h-16 rounded-2xl bg-white/80 backdrop-blur-md flex items-center justify-center mb-4 shadow-md">
                        <span class="material-symbols-outlined text-[#1D4ED8] text-4xl">handshake</span>
                    </div>
                    <div>
                        <div class="text-3xl font-extrabold mb-3">Mencegah Friksi Tim</div>
                        <div class="text-[#1E293B] font-semibold text-lg leading-relaxed">
                            Mengubah 49% potensi konflik antarkaryawan menjadi kekuatan kolaborasi melalui empati komunikasi.
                        </div>
                    </div>
                    <div class="inline-flex items-center gap-2 text-base font-black text-[#1E3A8A]">
                        <span>Buka Materi Presentasi</span>
                        <span class="material-symbols-outlined text-xl">arrow_forward</span>
                    </div>
                </div>
            </div>
        </div>
        """
    },

    # SLIDE 2: WORKPLACE REALITY
    {
        "id": 2,
        "category": "MODUL 1: REALITA & KEBUTUHAN",
        "title": "Realita Keberagaman di Tempat Kerja",
        "html": f"""
        <div class="h-full flex flex-col">
            {make_header("MODUL 1 • REALITA & KEBUTUHAN", "Realita Tempat Kerja: Menavigasi Kompleksitas Keberagaman", "Keberagaman Karyawan")}

            <div class="grid grid-cols-12 gap-8 flex-1">
                <!-- Card 1 (6 cols): Keberagaman yang Tak Terelakkan -->
                <div class="col-span-6 bg-white p-10 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between">
                    <div>
                        <div class="w-16 h-16 rounded-2xl bg-[#4F90F6]/15 text-[#2563EB] flex items-center justify-center mb-6">
                            <span class="material-symbols-outlined text-4xl">diversity_2</span>
                        </div>
                        <h3 class="text-3xl font-extrabold text-[#0D1B2A] mb-4">Keberagaman Adalah Kepastian</h3>
                        <p class="text-xl text-[#334155] leading-relaxed mb-6 font-medium">
                            Dalam suatu lingkup pekerjaan, tentu kita <strong>tidak bisa terlepas dari keberagaman</strong>. Kita setiap hari bekerja berdampingan dengan rekan pria maupun wanita, generasi senior maupun junior, dengan latar pendidikan, budaya, dan pola pikir yang berlainan.
                        </p>
                    </div>
                    <div class="p-5 rounded-2xl bg-[#F8FAFC] border-2 border-slate-200 flex items-start gap-4">
                        <span class="material-symbols-outlined text-[#2563EB] text-3xl mt-0.5">info</span>
                        <p class="text-base text-[#1E293B] font-semibold leading-relaxed">
                            Setiap orang membawa nilai kerja, cara berkomunikasi, dan gaya penyelesaian masalah yang berbeda ke meja kerja.
                        </p>
                    </div>
                </div>

                <!-- Card 2 (6 cols): Dua Arah Dampak Perbedaan -->
                <div class="col-span-6 bg-gradient-to-br from-[#F8FAFC] to-[#EFF6FF] p-10 rounded-[32px] border-2 border-[#9FBEED] shadow-md flex flex-col justify-between">
                    <div>
                        <div class="w-16 h-16 rounded-2xl bg-[#9FBEED]/40 text-[#1E40AF] flex items-center justify-center mb-6">
                            <span class="material-symbols-outlined text-4xl">sync_problem</span>
                        </div>
                        <h3 class="text-3xl font-extrabold text-[#0D1B2A] mb-4">Dua Arah Dampak Perbedaan</h3>
                        <p class="text-xl text-[#334155] leading-relaxed mb-6 font-medium">
                            Perbedaan karakter dapat menjadi <strong>kekuatan pendorong kemajuan</strong> jika dikelola secara terstruktur, atau menjadi <strong>sumber hambatan laten</strong> bila disikapi dengan ego pribadi.
                        </p>
                    </div>
                    
                    <div class="grid grid-cols-2 gap-5">
                        <div class="p-5 rounded-2xl bg-white border-2 border-rose-200 shadow-sm">
                            <div class="flex items-center gap-2 text-rose-700 font-extrabold text-base mb-2">
                                <span class="material-symbols-outlined text-xl">block</span> Tanpa Pemahaman
                            </div>
                            <p class="text-sm text-[#475569] font-medium leading-relaxed">Bentrokan ego antarbagian, saling curiga, dan melambatnya koordinasi kerja.</p>
                        </div>
                        <div class="p-5 rounded-2xl bg-white border-2 border-emerald-300 shadow-sm">
                            <div class="flex items-center gap-2 text-emerald-700 font-extrabold text-base mb-2">
                                <span class="material-symbols-outlined text-xl">check_circle</span> Dengan Framework
                            </div>
                            <p class="text-sm text-[#475569] font-medium leading-relaxed">Pembagian peran yang saling melengkapi, saling menghargai, dan hasil kerja optimal.</p>
                        </div>
                    </div>
                </div>

                <!-- Bottom 3 Pillars (12 cols) -->
                <div class="col-span-12 grid grid-cols-3 gap-6">
                    <div class="p-5 bg-white rounded-2xl border-2 border-slate-200 flex items-center gap-5 shadow-sm">
                        <div class="w-14 h-14 rounded-2xl bg-[#4F90F6]/15 text-[#2563EB] flex items-center justify-center flex-shrink-0">
                            <span class="material-symbols-outlined text-3xl">cake</span>
                        </div>
                        <div>
                            <div class="font-extrabold text-[#0D1B2A] text-lg">Lintas Usia & Generasi</div>
                            <div class="text-sm text-[#475569] font-medium">Pengalaman kerja, etos kerja, dan sudut pandang karir.</div>
                        </div>
                    </div>

                    <div class="p-5 bg-white rounded-2xl border-2 border-slate-200 flex items-center gap-5 shadow-sm">
                        <div class="w-14 h-14 rounded-2xl bg-[#9FBEED]/30 text-[#1E40AF] flex items-center justify-center flex-shrink-0">
                            <span class="material-symbols-outlined text-3xl">school</span>
                        </div>
                        <div>
                            <div class="font-extrabold text-[#0D1B2A] text-lg">Pola Pikir & Latar Belakang</div>
                            <div class="text-sm text-[#475569] font-medium">Latar pendidikan teknis vs konseptual dalam memandang persoalan.</div>
                        </div>
                    </div>

                    <div class="p-5 bg-white rounded-2xl border-2 border-slate-200 flex items-center gap-5 shadow-sm">
                        <div class="w-14 h-14 rounded-2xl bg-[#4F90F6]/20 text-[#2563EB] flex items-center justify-center flex-shrink-0">
                            <span class="material-symbols-outlined text-3xl">psychology_alt</span>
                        </div>
                        <div>
                            <div class="font-extrabold text-[#0D1B2A] text-lg">Kepribadian Unik</div>
                            <div class="text-sm text-[#475569] font-medium">Cara mengambil keputusan dan respon alami terhadap tekanan tugas.</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
    },

    # SLIDE 3: DATA KASUS
    {
        "id": 3,
        "category": "MODUL 1: REALITA & KEBUTUHAN",
        "title": "Fakta Data: Akar Utama Konflik Kerja",
        "html": f"""
        <div class="h-full flex flex-col">
            {make_header("MODUL 1 • REALITA & KEBUTUHAN", "Fakta Data: Bentrokan Kepribadian Adalah Akar Konflik", "Faktor Risiko Tertinggi", "bg-rose-50 text-rose-700 border-rose-200")}

            <div class="grid grid-cols-12 gap-8 flex-1">
                <!-- Left Hero Stat (5 cols) -->
                <div class="col-span-5 bg-gradient-to-br from-[#4F90F6] via-[#2563EB] to-[#1D4ED8] p-12 rounded-[32px] text-white shadow-2xl flex flex-col justify-between relative overflow-hidden">
                    <div class="absolute -right-12 -bottom-12 w-72 h-72 bg-white/10 rounded-full blur-2xl pointer-events-none"></div>
                    
                    <div>
                        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/20 backdrop-blur-md text-white font-extrabold text-sm uppercase tracking-wider mb-6">
                            <span class="material-symbols-outlined text-lg">pie_chart</span>
                            Temuan Utama Riset
                        </div>
                        <div class="text-9xl font-black tracking-tighter leading-none mb-6">49%</div>
                        <h3 class="text-3xl font-extrabold leading-snug mb-4">
                            Pegawai Kantor Menyatakan Bentrokan Kepribadian Sebagai Penyebab Utama Konflik.
                        </h3>
                        <p class="text-white/90 text-xl leading-relaxed font-medium">
                            Sebagian besar gesekan bukan disebabkan oleh kurangnya kemampuan teknis, melainkan ketidakcocokan cara komunikasi dan benturan ego antarkaryawan.
                        </p>
                    </div>

                    <div class="pt-6 border-t border-white/25 text-sm text-white/80 font-medium">
                        Sumber: Workplace Conflict and How Businesses Can Harness It to Thrive (Riset CPP Global, melibatkan ribuan profesional).
                    </div>
                </div>

                <!-- Right Comparison & Drivers (7 cols) -->
                <div class="col-span-7 flex flex-col gap-6">
                    <!-- Top Chart Card -->
                    <div class="bg-white p-8 rounded-[32px] border-2 border-slate-200 shadow-md flex-1 flex flex-col justify-between">
                        <div class="flex items-center justify-between mb-4">
                            <h4 class="font-extrabold text-[#0D1B2A] text-2xl">Pemicu Konflik di Tempat Kerja:</h4>
                            <span class="text-sm font-bold text-[#64748B]">% Pegawai Terdampak</span>
                        </div>

                        <!-- Bar rows with enlarged labels -->
                        <div class="space-y-4">
                            <div>
                                <div class="flex justify-between text-base font-extrabold text-[#0D1B2A] mb-1.5">
                                    <span class="flex items-center gap-2 text-[#2563EB]"><span class="material-symbols-outlined text-xl">error</span> Bentrokan Kepribadian & Ego (Personality Clashes)</span>
                                    <span class="text-lg">49%</span>
                                </div>
                                <div class="w-full bg-slate-100 rounded-full h-4 overflow-hidden border border-slate-200">
                                    <div class="bg-gradient-to-r from-[#4F90F6] to-[#2563EB] h-4 rounded-full" style="width: 49%"></div>
                                </div>
                            </div>

                            <div>
                                <div class="flex justify-between text-base font-bold text-[#334155] mb-1.5">
                                    <span>Beban Stres Kerja</span>
                                    <span>34%</span>
                                </div>
                                <div class="w-full bg-slate-100 rounded-full h-3 overflow-hidden">
                                    <div class="bg-[#9FBEED] h-3 rounded-full" style="width: 34%"></div>
                                </div>
                            </div>

                            <div>
                                <div class="flex justify-between text-base font-bold text-[#334155] mb-1.5">
                                    <span>Beban Tugas Terlalu Berat / Keterbatasan Sumber Daya</span>
                                    <span>33%</span>
                                </div>
                                <div class="w-full bg-slate-100 rounded-full h-3 overflow-hidden">
                                    <div class="bg-[#9FBEED] h-3 rounded-full" style="width: 33%"></div>
                                </div>
                            </div>

                            <div>
                                <div class="flex justify-between text-base font-bold text-[#334155] mb-1.5">
                                    <span>Kepemimpinan Kurang Efektif dari Pimpinan</span>
                                    <span>29%</span>
                                </div>
                                <div class="w-full bg-slate-100 rounded-full h-3 overflow-hidden">
                                    <div class="bg-slate-300 h-3 rounded-full" style="width: 29%"></div>
                                </div>
                            </div>

                            <div>
                                <div class="flex justify-between text-base font-bold text-[#334155] mb-1.5">
                                    <span>Kurangnya Keterbukaan & Kejujuran Antarrekan</span>
                                    <span>26%</span>
                                </div>
                                <div class="w-full bg-slate-100 rounded-full h-3 overflow-hidden">
                                    <div class="bg-slate-300 h-3 rounded-full" style="width: 26%"></div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Bottom Insight Card -->
                    <div class="p-6 rounded-2xl bg-gradient-to-r from-[#EFF6FF] via-[#E2EEFE] to-[#D5E6FC] border-2 border-[#9FBEED] flex items-center gap-6 shadow-sm">
                        <div class="w-16 h-16 rounded-2xl bg-[#2563EB] text-white flex items-center justify-center flex-shrink-0 shadow-md">
                            <span class="material-symbols-outlined text-3xl">hourglass_empty</span>
                        </div>
                        <div>
                            <div class="font-black text-[#0D1B2A] text-xl mb-1">Dampak Nyata: 2,8 Jam Terbuang Tiap Minggu</div>
                            <div class="text-base text-[#334155] font-medium leading-relaxed">
                                Setiap karyawan rata-rata menghabiskan hampir 3 jam per minggu terseret dalam gesekan interpersonal. Memahami tipe kepribadian adalah langkah pencegahan paling hemat biaya.
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
    },

    # SLIDE 4: APA ITU PERSONALITY?
    {
        "id": 4,
        "category": "MODUL 1: REALITA & KEBUTUHAN",
        "title": "Mengenal Personality: Trait Alami vs Perilaku",
        "html": f"""
        <div class="h-full flex flex-col">
            {make_header("MODUL 1 • REALITA & KEBUTUHAN", "Personality: Sifat Dasar (Trait) vs Perilaku Kerja", "Karakteristik Alami")}

            <div class="grid grid-cols-3 gap-8 flex-1">
                <!-- Pillar 1: Definition -->
                <div class="bg-white p-9 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between">
                    <div>
                        <div class="w-16 h-16 rounded-2xl bg-[#4F90F6]/15 text-[#2563EB] flex items-center justify-center mb-6">
                            <span class="material-symbols-outlined text-4xl">fingerprint</span>
                        </div>
                        <h3 class="text-3xl font-extrabold text-[#0D1B2A] mb-4">Definisi Personality</h3>
                        <p class="text-lg text-[#334155] leading-relaxed mb-6 font-medium">
                            Personality dibentuk dari beberapa <strong>traits permanen</strong> yang menjadikan setiap individu memiliki karakteristik khas dalam cara berpikir, merasa, dan mengambil tindakan.
                        </p>
                        <div class="space-y-4">
                            <div class="flex items-center gap-3 text-base text-[#1E293B] font-bold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl">check_circle</span>
                                Cenderung stabil sepanjang usia dewasa
                            </div>
                            <div class="flex items-center gap-3 text-base text-[#1E293B] font-bold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl">check_circle</span>
                                Menjadi lensa otomatis saat merespon situasi
                            </div>
                            <div class="flex items-center gap-3 text-base text-[#1E293B] font-bold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl">check_circle</span>
                                Bukan batas kecerdasan maupun kompetensi teknis
                            </div>
                        </div>
                    </div>
                    <div class="p-4 rounded-2xl bg-[#F8FAFC] border-2 border-slate-200 text-sm text-[#475569] font-medium leading-relaxed">
                        💡 <em>"Sifat bawaan adalah rancangan kabel alami pikiran kita; kebiasaan adalah cara kita memanfaatkannya."</em>
                    </div>
                </div>

                <!-- Pillar 2: The Core Trait Spectrum (Featured) -->
                <div class="bg-gradient-to-b from-[#EFF6FF] via-[#E2EEFE] to-[#D0E4FB] p-9 rounded-[32px] border-2 border-[#9FBEED] shadow-lg flex flex-col justify-between">
                    <div>
                        <div class="w-16 h-16 rounded-2xl bg-[#2563EB] text-white flex items-center justify-center mb-6 shadow-md">
                            <span class="material-symbols-outlined text-4xl">tune</span>
                        </div>
                        <h3 class="text-3xl font-extrabold text-[#0D1B2A] mb-3">Spektrum Karakter</h3>
                        <p class="text-base text-[#334155] leading-relaxed mb-6 font-medium">
                            Setiap orang berada di titik unik pada spektrum karakter. Tidak ada sifat yang salah atau benar:
                        </p>
                        <div class="grid grid-cols-2 gap-3.5">
                            <div class="p-3.5 bg-white/90 backdrop-blur rounded-2xl border border-white text-center shadow-sm">
                                <div class="font-black text-[#0D1B2A] text-base">Brave</div>
                                <div class="text-xs text-[#64748B] font-bold">Berani Ambil Risiko</div>
                            </div>
                            <div class="p-3.5 bg-white/90 backdrop-blur rounded-2xl border border-white text-center shadow-sm">
                                <div class="font-black text-[#0D1B2A] text-base">Reserved</div>
                                <div class="text-xs text-[#64748B] font-bold">Cermat & Berhati-hati</div>
                            </div>
                            <div class="p-3.5 bg-white/90 backdrop-blur rounded-2xl border border-white text-center shadow-sm">
                                <div class="font-black text-[#0D1B2A] text-base">Aggressive</div>
                                <div class="text-xs text-[#64748B] font-bold">Dorongan Hasil Tinggi</div>
                            </div>
                            <div class="p-3.5 bg-white/90 backdrop-blur rounded-2xl border border-white text-center shadow-sm">
                                <div class="font-black text-[#0D1B2A] text-base">Calm / Shy</div>
                                <div class="text-xs text-[#64748B] font-bold">Pengamat yang Tenang</div>
                            </div>
                            <div class="p-3.5 bg-white/90 backdrop-blur rounded-2xl border border-white text-center shadow-sm">
                                <div class="font-black text-[#0D1B2A] text-base">Cheerful</div>
                                <div class="text-xs text-[#64748B] font-bold">Membangun Semangat</div>
                            </div>
                            <div class="p-3.5 bg-white/90 backdrop-blur rounded-2xl border border-white text-center shadow-sm">
                                <div class="font-black text-[#0D1B2A] text-base">Realistic</div>
                                <div class="text-xs text-[#64748B] font-bold">Fokus Pada Fakta Nyata</div>
                            </div>
                        </div>
                    </div>
                    <div class="p-4 rounded-2xl bg-white/70 text-sm text-[#1E3A8A] font-extrabold text-center">
                        Masing-masing karakter memiliki keunggulan spesifik pada tugas yang tepat.
                    </div>
                </div>

                <!-- Pillar 3: Workplace Impact -->
                <div class="bg-white p-9 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between">
                    <div>
                        <div class="w-16 h-16 rounded-2xl bg-[#9FBEED]/40 text-[#1E40AF] flex items-center justify-center mb-6">
                            <span class="material-symbols-outlined text-4xl">workspaces</span>
                        </div>
                        <h3 class="text-3xl font-extrabold text-[#0D1B2A] mb-4">Pengaruh di Dunia Kerja</h3>
                        <p class="text-lg text-[#334155] leading-relaxed mb-6 font-medium">
                            Bagaimana kepribadian langsung mempengaruhi ritme operasional sehari-hari:
                        </p>
                        <div class="space-y-4">
                            <div class="p-4 rounded-2xl bg-[#F8FAFC] border border-slate-200">
                                <div class="font-extrabold text-[#0D1B2A] text-base mb-1 flex items-center gap-2">
                                    <span class="material-symbols-outlined text-[#2563EB] text-xl">forum</span>
                                    Gaya Komunikasi
                                </div>
                                <div class="text-sm text-[#475569] font-medium">Apakah berbicara lugas to-the-point atau membutuhkan pendekatan personal terlebih dahulu.</div>
                            </div>
                            <div class="p-4 rounded-2xl bg-[#F8FAFC] border border-slate-200">
                                <div class="font-extrabold text-[#0D1B2A] text-base mb-1 flex items-center gap-2">
                                    <span class="material-symbols-outlined text-[#2563EB] text-xl">speed</span>
                                    Kecepatan Eksekusi
                                </div>
                                <div class="text-sm text-[#475569] font-medium">Apakah langsung mencoba di lapangan atau menelaah data secara menyeluruh sebelum bertindak.</div>
                            </div>
                            <div class="p-4 rounded-2xl bg-[#F8FAFC] border border-slate-200">
                                <div class="font-extrabold text-[#0D1B2A] text-base mb-1 flex items-center gap-2">
                                    <span class="material-symbols-outlined text-[#2563EB] text-xl">psychology</span>
                                    Respon Saat Krisis
                                </div>
                                <div class="text-sm text-[#475569] font-medium">Bagaimana ketahanan emosional menghadapi perubahan rencana mendadak.</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
    },

    # SLIDE 5: METODE ASESMEN
    {
        "id": 5,
        "category": "MODUL 1: REALITA & KEBUTUHAN",
        "title": "Cara Menemukan Personality: Subjektif vs Objektif",
        "html": f"""
        <div class="h-full flex flex-col">
            {make_header("MODUL 1 • REALITA & KEBUTUHAN", "How To Find Your Personality: Pendekatan Subjektif vs Objektif", "Dua Jalur Penilaian")}

            <div class="grid grid-cols-2 gap-8 flex-1">
                <!-- Method 01: Subjektif -->
                <div class="bg-white p-10 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-6">
                            <span class="px-4 py-1.5 rounded-full bg-slate-100 text-[#334155] font-black text-sm uppercase tracking-wider">
                                JALUR 01 • SUBJEKTIF
                            </span>
                            <div class="w-14 h-14 rounded-2xl bg-slate-100 text-[#475569] flex items-center justify-center">
                                <span class="material-symbols-outlined text-3xl">visibility</span>
                            </div>
                        </div>
                        <h3 class="text-3xl font-extrabold text-[#0D1B2A] mb-3">Pendekatan Pengamatan Langsung</h3>
                        <p class="text-lg text-[#475569] mb-6 font-medium">Identifikasi melalui pengamatan perilaku sehari-hari dan interaksi percakapan tatap muka.</p>
                        
                        <div class="space-y-5">
                            <div class="p-6 rounded-2xl bg-[#F8FAFC] border-2 border-slate-200 flex items-start gap-4">
                                <span class="material-symbols-outlined text-[#2563EB] text-3xl mt-0.5">remove_red_eye</span>
                                <div>
                                    <div class="font-extrabold text-[#0D1B2A] text-lg mb-1">Observasi Perilaku Keseharian</div>
                                    <div class="text-base text-[#475569] font-medium leading-relaxed">Melihat respon spontan saat rapat, cara bersosialisasi, atau ketenangan saat dikejar batas waktu.</div>
                                </div>
                            </div>

                            <div class="p-6 rounded-2xl bg-[#F8FAFC] border-2 border-slate-200 flex items-start gap-4">
                                <span class="material-symbols-outlined text-[#2563EB] text-3xl mt-0.5">record_voice_over</span>
                                <div>
                                    <div class="font-extrabold text-[#0D1B2A] text-lg mb-1">Wawancara & Dialog 1-on-1</div>
                                    <div class="text-base text-[#475569] font-medium leading-relaxed">Menggali motivasi dari dalam diri, impian kerja, dan hal-hal yang memicu ketidaknyamanan lewat obrolan mendalam.</div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="p-4 rounded-2xl bg-amber-50 border-2 border-amber-200 flex items-center gap-3 text-amber-900 text-sm font-semibold">
                        <span class="material-symbols-outlined text-2xl flex-shrink-0 text-amber-700">warning</span>
                        <span><strong>Tantangan:</strong> Rentan bias asumsi pribadi, kesan pertama yang keliru, dan pengaruh suasana hati sesaat.</span>
                    </div>
                </div>

                <!-- Method 02: Objektif -->
                <div class="bg-gradient-to-br from-white via-[#F8FAFC] to-[#EFF6FF] p-10 rounded-[32px] border-2 border-[#4F90F6] shadow-xl flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-6">
                            <span class="px-4 py-1.5 rounded-full bg-[#4F90F6]/20 text-[#1D4ED8] font-black text-sm uppercase tracking-wider">
                                JALUR 02 • OBJEKTIF & TERSTANDAR
                            </span>
                            <div class="w-14 h-14 rounded-2xl bg-[#2563EB] text-white flex items-center justify-center shadow-md">
                                <span class="material-symbols-outlined text-3xl">verified</span>
                            </div>
                        </div>
                        <h3 class="text-3xl font-extrabold text-[#0D1B2A] mb-3">Instrumen & Alat Tes Psikometri</h3>
                        <p class="text-lg text-[#475569] mb-6 font-medium">Pengukuran berbasis kuesioner teruji secara ilmiah dengan metode penilaian baku.</p>
                        
                        <div class="grid grid-cols-2 gap-4 mb-6">
                            <div class="p-5 rounded-2xl bg-white border-2 border-[#2563EB] shadow-md">
                                <div class="flex items-center justify-between mb-2">
                                    <span class="font-black text-[#2563EB] text-2xl">MBTI</span>
                                    <span class="px-2.5 py-1 rounded-md text-xs font-black bg-[#4F90F6]/15 text-[#1D4ED8]">Fokus Utama</span>
                                </div>
                                <p class="text-sm text-[#334155] font-semibold leading-relaxed">Memetakan 16 tipe preferensi kognitif (Jungian Typology).</p>
                            </div>

                            <div class="p-5 rounded-2xl bg-white border-2 border-slate-200 shadow-sm">
                                <div class="font-black text-[#0D1B2A] text-xl mb-2">DISC</div>
                                <p class="text-sm text-[#475569] font-medium leading-relaxed">Mengukur gaya perilaku kerja: Dominance, Influence, Steadiness, Conscientiousness.</p>
                            </div>

                            <div class="p-5 rounded-2xl bg-white border-2 border-slate-200 shadow-sm">
                                <div class="font-black text-[#0D1B2A] text-xl mb-2">HEXACO</div>
                                <p class="text-sm text-[#475569] font-medium leading-relaxed">6 Dimensi karakter moral, kestabilan emosi, dan keterbukaan ide.</p>
                            </div>

                            <div class="p-5 rounded-2xl bg-white border-2 border-slate-200 shadow-sm">
                                <div class="font-black text-[#0D1B2A] text-xl mb-2">NEO™-PI-3</div>
                                <p class="text-sm text-[#475569] font-medium leading-relaxed">Standar baku Big Five Personality untuk asesmen kepemimpinan.</p>
                            </div>
                        </div>
                    </div>

                    <div class="p-4 rounded-2xl bg-[#E6F0FD] border-2 border-[#9FBEED] flex items-center gap-3 text-[#1E3A8A] text-sm font-bold">
                        <span class="material-symbols-outlined text-2xl text-[#2563EB] flex-shrink-0">check_circle</span>
                        <span>Memberikan bahasa bersama <em>(shared vocabulary)</em> yang netral tanpa penghakiman negatif.</span>
                    </div>
                </div>
            </div>
        </div>
        """
    },

    # SLIDE 6: SEJARAH & TUJUAN MBTI
    {
        "id": 6,
        "category": "MODUL 2: FRAMEWORK MBTI",
        "title": "Mengenal MBTI: Sejarah & Landasan Carl Jung",
        "html": f"""
        <div class="h-full flex flex-col">
            {make_header("MODUL 2 • FRAMEWORK MBTI", "MBTI: Myers-Briggs Type Indicator", "Sejarah & Nilai Organisasi")}

            <div class="grid grid-cols-12 gap-8 flex-1">
                <!-- Card 1 (7 cols Top): History & Theory -->
                <div class="col-span-7 bg-white p-9 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between">
                    <div>
                        <div class="w-16 h-16 rounded-2xl bg-[#4F90F6]/15 text-[#2563EB] flex items-center justify-center mb-5">
                            <span class="material-symbols-outlined text-4xl">history_edu</span>
                        </div>
                        <h3 class="text-3xl font-extrabold text-[#0D1B2A] mb-4">Sejarah & Landasan Teori</h3>
                        <p class="text-lg text-[#334155] leading-relaxed mb-4 font-medium">
                            MBTI adalah instrumen psikologis berupa <em>self-report questionnaire</em> yang dirancang oleh <strong>Katharine Cook Briggs</strong> dan putrinya, <strong>Isabel Briggs Myers</strong> pada tahun 1940-an.
                        </p>
                        <p class="text-lg text-[#334155] leading-relaxed font-medium">
                            Instrumen ini terinspirasi langsung dari teori tipologi kepribadian tokoh psikologi dunia <strong>Carl Gustav Jung</strong> dalam karyanya <em>"Psychological Types"</em> (1921).
                        </p>
                    </div>

                    <div class="pt-5 border-t-2 border-slate-100 flex items-center gap-3 text-sm font-bold text-[#475569]">
                        <span class="material-symbols-outlined text-[#2563EB] text-2xl">verified</span>
                        Dipercaya dan diterapkan oleh lebih dari 88% perusahaan Fortune 500 untuk pembinaan tim kerja.
                    </div>
                </div>

                <!-- Card 2 (5 cols Top): Core Purpose (Hero Blue) -->
                <div class="col-span-5 bg-gradient-to-br from-[#4F90F6] via-[#2563EB] to-[#1D4ED8] p-9 rounded-[32px] text-white shadow-xl flex flex-col justify-between">
                    <div>
                        <div class="w-16 h-16 rounded-2xl bg-white/20 backdrop-blur flex items-center justify-center mb-5">
                            <span class="material-symbols-outlined text-4xl">lightbulb</span>
                        </div>
                        <h3 class="text-3xl font-extrabold mb-4">Tujuan Utama MBTI</h3>
                        <p class="text-white/95 text-lg leading-relaxed mb-5 font-medium">
                            MBTI <strong>bukan untuk memberi label kaku</strong> pada diri seseorang, melainkan untuk:
                        </p>
                        <ul class="space-y-3 text-base text-white/95 font-semibold">
                            <li class="flex items-center gap-3">
                                <span class="material-symbols-outlined text-lg">check_circle</span>
                                Memahami pola dasar fungsi mental manusia.
                            </li>
                            <li class="flex items-center gap-3">
                                <span class="material-symbols-outlined text-lg">check_circle</span>
                                Menemukan motivasi kerja dan potensi alami.
                            </li>
                            <li class="flex items-center gap-3">
                                <span class="material-symbols-outlined text-lg">check_circle</span>
                                Membangun kerja sama yang saling menguatkan.
                            </li>
                        </ul>
                    </div>
                    <div class="text-sm text-white/80 font-medium">
                        "Setiap tipe kepribadian memiliki keunggulan tersendiri yang bernilai bagi kemajuan tim."
                    </div>
                </div>

                <!-- Card 3 (6 cols Bottom): Manfaat Bagi Individu -->
                <div class="col-span-6 bg-[#F8FAFC] p-8 rounded-[32px] border-2 border-slate-200 flex items-start gap-5 shadow-sm">
                    <div class="w-16 h-16 rounded-2xl bg-emerald-100 text-emerald-800 flex items-center justify-center flex-shrink-0">
                        <span class="material-symbols-outlined text-4xl">person</span>
                    </div>
                    <div>
                        <h4 class="font-black text-[#0D1B2A] text-2xl mb-2">Manfaat Bagi Individu</h4>
                        <p class="text-base text-[#475569] leading-relaxed font-medium">
                            Membantu mengenali kekuatan alami diri, menyadari area yang rentan terhadap stres, dan menemukan cara kerja yang paling nyaman serta produktif.
                        </p>
                    </div>
                </div>

                <!-- Card 4 (6 cols Bottom): Manfaat Bagi Tim & Organisasi -->
                <div class="col-span-6 bg-[#F8FAFC] p-8 rounded-[32px] border-2 border-slate-200 flex items-start gap-5 shadow-sm">
                    <div class="w-16 h-16 rounded-2xl bg-[#9FBEED]/40 text-[#1E40AF] flex items-center justify-center flex-shrink-0">
                        <span class="material-symbols-outlined text-4xl">groups_2</span>
                    </div>
                    <div>
                        <h4 class="font-black text-[#0D1B2A] text-2xl mb-2">Manfaat Bagi Tim & Perusahaan</h4>
                        <p class="text-base text-[#475569] leading-relaxed font-medium">
                            Mencegah kesalahpahaman antardivisi, menempatkan orang pada penugasan yang pas <em>(job fit)</em>, dan menjaga kestabilan iklim kerja.
                        </p>
                    </div>
                </div>
            </div>
        </div>
        """
    },

    # SLIDE 7: 4 DIMENSI KOMPAS
    {
        "id": 7,
        "category": "MODUL 2: FRAMEWORK MBTI",
        "title": "4 Dimensi Kepribadian MBTI",
        "html": f"""
        <div class="h-full flex flex-col">
            {make_header("MODUL 2 • FRAMEWORK MBTI", "Simplify MBTI: 4 Dimensi Dasar Kepribadian", "4 Pertanyaan Penentu")}

            <div class="grid grid-cols-2 gap-8 flex-1">
                <!-- Dimensi 1: Energy -->
                <div class="bg-white p-8 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between hover:border-[#4F90F6] transition-all">
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <span class="px-4 py-1.5 rounded-full bg-[#4F90F6]/15 text-[#1D4ED8] font-black text-sm">
                                DIMENSI 01 • SUMBER ENERGI
                            </span>
                            <span class="material-symbols-outlined text-4xl text-[#2563EB]">battery_charging_full</span>
                        </div>
                        <h3 class="text-2xl font-extrabold text-[#0D1B2A] mb-2">Introversion (I) vs Extraversion (E)</h3>
                        <p class="text-base text-[#64748B] font-medium mb-5">Ke mana arah perhatian utama Anda dan bagaimana Anda mengisi ulang energi mental?</p>
                        
                        <div class="grid grid-cols-2 gap-4">
                            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200">
                                <div class="font-black text-[#0D1B2A] text-base mb-1">Introversion [I]</div>
                                <div class="text-sm text-[#475569] font-medium leading-relaxed">Fokus ke dalam diri, refleksi tenang, dan pemikiran mendalam mandiri.</div>
                            </div>
                            <div class="p-4 rounded-2xl bg-[#EFF6FF] border border-[#9FBEED]">
                                <div class="font-black text-[#1E40AF] text-base mb-1">Extraversion [E]</div>
                                <div class="text-sm text-[#475569] font-medium leading-relaxed">Fokus ke dunia luar, interaksi sosial aktif, dan beraksi bersama orang lain.</div>
                            </div>
                        </div>
                    </div>
                    <div class="text-sm font-black text-[#334155] pt-4 border-t border-slate-100 flex items-center gap-2">
                        <span class="material-symbols-outlined text-lg text-[#2563EB]">bolt</span>
                        Kata Kunci: <strong>ENERGY (Sumber Energi Mental)</strong>
                    </div>
                </div>

                <!-- Dimensi 2: Information -->
                <div class="bg-white p-8 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between hover:border-[#4F90F6] transition-all">
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <span class="px-4 py-1.5 rounded-full bg-[#9FBEED]/40 text-[#1E40AF] font-black text-sm">
                                DIMENSI 02 • PENYERAPAN FAKTA
                            </span>
                            <span class="material-symbols-outlined text-4xl text-[#2563EB]">filter_center_focus</span>
                        </div>
                        <h3 class="text-2xl font-extrabold text-[#0D1B2A] mb-2">Sensing (S) vs Intuition (N)</h3>
                        <p class="text-base text-[#64748B] font-medium mb-5">Jenis data seperti apa yang secara alami diperhatikan dan dipercaya oleh pikiran Anda?</p>
                        
                        <div class="grid grid-cols-2 gap-4">
                            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200">
                                <div class="font-black text-[#0D1B2A] text-base mb-1">Sensing [S]</div>
                                <div class="text-sm text-[#475569] font-medium leading-relaxed">Fakta konkret yang nyata, bukti data riil, dan hal-hal yang bersifat praktis.</div>
                            </div>
                            <div class="p-4 rounded-2xl bg-[#EFF6FF] border border-[#9FBEED]">
                                <div class="font-black text-[#1E40AF] text-base mb-1">Intuition [N]</div>
                                <div class="text-sm text-[#475569] font-medium leading-relaxed">Gambaran besar (big picture), pola tersembunyi, dan peluang masa depan.</div>
                            </div>
                        </div>
                    </div>
                    <div class="text-sm font-black text-[#334155] pt-4 border-t border-slate-100 flex items-center gap-2">
                        <span class="material-symbols-outlined text-lg text-[#2563EB]">dataset</span>
                        Kata Kunci: <strong>INFORMATION (Cara Membaca Fakta)</strong>
                    </div>
                </div>

                <!-- Dimensi 3: Decision Making -->
                <div class="bg-white p-8 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between hover:border-[#4F90F6] transition-all">
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <span class="px-4 py-1.5 rounded-full bg-slate-100 text-[#334155] font-black text-sm">
                                DIMENSI 03 • CARA MEMUTUSKAN
                            </span>
                            <span class="material-symbols-outlined text-4xl text-[#2563EB]">balance</span>
                        </div>
                        <h3 class="text-2xl font-extrabold text-[#0D1B2A] mb-2">Thinking (T) vs Feeling (F)</h3>
                        <p class="text-base text-[#64748B] font-medium mb-5">Pedoman apa yang Anda gunakan saat harus menarik kesimpulan atau keputusan akhir?</p>
                        
                        <div class="grid grid-cols-2 gap-4">
                            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200">
                                <div class="font-black text-[#0D1B2A] text-base mb-1">Thinking [T]</div>
                                <div class="text-sm text-[#475569] font-medium leading-relaxed">Analisis sebab-akibat yang logis, kriteria objektif, dan efisiensi sistem.</div>
                            </div>
                            <div class="p-4 rounded-2xl bg-[#EFF6FF] border border-[#9FBEED]">
                                <div class="font-black text-[#1E40AF] text-base mb-1">Feeling [F]</div>
                                <div class="text-sm text-[#475569] font-medium leading-relaxed">Nilai kemanusiaan, empati perasaan, dampak sosial, dan keharmonisan tim.</div>
                            </div>
                        </div>
                    </div>
                    <div class="text-sm font-black text-[#334155] pt-4 border-t border-slate-100 flex items-center gap-2">
                        <span class="material-symbols-outlined text-lg text-[#2563EB]">gavel</span>
                        Kata Kunci: <strong>DECISION MAKING (Pengambilan Keputusan)</strong>
                    </div>
                </div>

                <!-- Dimensi 4: Lifestyle -->
                <div class="bg-white p-8 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between hover:border-[#4F90F6] transition-all">
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <span class="px-4 py-1.5 rounded-full bg-[#4F90F6]/15 text-[#1D4ED8] font-black text-sm">
                                DIMENSI 04 • PENATAAN WAKTU
                            </span>
                            <span class="material-symbols-outlined text-4xl text-[#2563EB]">calendar_month</span>
                        </div>
                        <h3 class="text-2xl font-extrabold text-[#0D1B2A] mb-2">Judging (J) vs Perceiving (P)</h3>
                        <p class="text-base text-[#64748B] font-medium mb-5">Bagaimana cara Anda menata jadwal, rencana kerja, dan merespon perubahan luar?</p>
                        
                        <div class="grid grid-cols-2 gap-4">
                            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200">
                                <div class="font-black text-[#0D1B2A] text-base mb-1">Judging [J]</div>
                                <div class="text-sm text-[#475569] font-medium leading-relaxed">Teratur, jadwal rapi, menyukai kepastian, dan disiplin tenggat waktu.</div>
                            </div>
                            <div class="p-4 rounded-2xl bg-[#EFF6FF] border border-[#9FBEED]">
                                <div class="font-black text-[#1E40AF] text-base mb-1">Perceiving [P]</div>
                                <div class="text-sm text-[#475569] font-medium leading-relaxed">Spontan, fleksibel terhadap alur kerja, terbuka pada pilihan alternatif baru.</div>
                            </div>
                        </div>
                    </div>
                    <div class="text-sm font-black text-[#334155] pt-4 border-t border-slate-100 flex items-center gap-2">
                        <span class="material-symbols-outlined text-lg text-[#2563EB]">navigation</span>
                        Kata Kunci: <strong>APPROACH TO WORLD (Pola Penataan Kerja)</strong>
                    </div>
                </div>
            </div>
        </div>
        """
    },

    # SLIDE 8: DEEP DIVE E vs I
    {
        "id": 8,
        "category": "MODUL 2: FRAMEWORK MBTI",
        "title": "Dimensi 1 (Energi): Extraversion vs Introversion",
        "html": f"""
        <div class="h-full flex flex-col">
            {make_header("MODUL 2 • FRAMEWORK MBTI", "Introversion (I) vs Extraversion (E)", "Dua Cara Mengisi Ulang Daya Mental")}

            <div class="grid grid-cols-2 gap-8 flex-1">
                <!-- Card 1: Introversion (I) -->
                <div class="bg-white p-10 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-6">
                            <div class="flex items-center gap-4">
                                <div class="w-16 h-16 rounded-2xl bg-[#0D1B2A] text-white flex items-center justify-center font-black text-3xl">
                                    I
                                </div>
                                <div>
                                    <h3 class="text-3xl font-extrabold text-[#0D1B2A]">Introversion</h3>
                                    <span class="text-base text-[#64748B] font-bold">Fokus Energi Pada Refleksi Batin</span>
                                </div>
                            </div>
                            <span class="material-symbols-outlined text-4xl text-slate-400">nightlight</span>
                        </div>

                        <p class="text-lg text-[#334155] leading-relaxed mb-6 font-medium">
                            Mengarahkan perhatian ke dalam dunia ide dan pemikiran pribadi. Mengisi energi melalui ketenangan, perenungan mendalam, dan sesi analisis mandiri tanpa gangguan.
                        </p>

                        <div class="space-y-4">
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">edit_note</span>
                                <span>Lebih nyaman berkomunikasi secara tertulis (email, memo, laporan terstruktur).</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">psychology</span>
                                <span>Berpikir matang terlebih dahulu sebelum menyatakan pendapat di forum.</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">center_focus_strong</span>
                                <span>Fokus secara mendalam pada hal-hal penting (mengutamakan kedalaman daripada keluasan).</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">lock</span>
                                <span>Cenderung tertutup dan baru mengambil inisiatif saat situasi benar-benar mendesak.</span>
                            </div>
                        </div>
                    </div>

                    <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 text-sm text-[#475569] font-bold">
                        💡 <strong>Tips Kolaborasi:</strong> Berikan materi rapat sehari sebelumnya agar mereka memiliki waktu membaca dan menyiapkan analisis terbaiknya.
                    </div>
                </div>

                <!-- Card 2: Extraversion (E) -->
                <div class="bg-gradient-to-br from-white to-[#EFF6FF] p-10 rounded-[32px] border-2 border-[#4F90F6] shadow-xl flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-6">
                            <div class="flex items-center gap-4">
                                <div class="w-16 h-16 rounded-2xl bg-[#2563EB] text-white flex items-center justify-center font-black text-3xl shadow-md">
                                    E
                                </div>
                                <div>
                                    <h3 class="text-3xl font-extrabold text-[#0D1B2A]">Extraversion</h3>
                                    <span class="text-base text-[#1D4ED8] font-bold">Fokus Energi Pada Aksi Eksternal</span>
                                </div>
                            </div>
                            <span class="material-symbols-outlined text-4xl text-amber-500">wb_sunny</span>
                        </div>

                        <p class="text-lg text-[#334155] leading-relaxed mb-6 font-medium">
                            Selaras dengan lingkungan sekitar. Memperoleh energi melalui obrolan langsung dengan orang lain, berdiskusi kelompok secara aktif, dan segera mengambil langkah nyata.
                        </p>

                        <div class="space-y-4">
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">record_voice_over</span>
                                <span>Lebih suka berkomunikasi lewat tatap muka langsung, telepon, atau diskusi lisan.</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">group_work</span>
                                <span>Menyempurnakan gagasan sambil berbicara dan berdialog aktif dengan rekan tim.</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">hub</span>
                                <span>Mempunyai jaringan ketertarikan yang luas (keluasan topik yang beragam).</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">bolt</span>
                                <span>Mudah bergaul, ekspresif, dan sigap mengambil inisiatif dalam dinamika tim.</span>
                            </div>
                        </div>
                    </div>

                    <div class="p-5 rounded-2xl bg-[#E6F0FD] border border-[#9FBEED] text-sm text-[#1E3A8A] font-bold">
                        💡 <strong>Tips Kolaborasi:</strong> Libatkan mereka dalam forum tukar pendapat untuk memicu semangat dan mencairkan suasana kerja tim.
                    </div>
                </div>
            </div>
        </div>
        """
    },

    # SLIDE 9: DEEP DIVE S vs N
    {
        "id": 9,
        "category": "MODUL 2: FRAMEWORK MBTI",
        "title": "Dimensi 2 (Informasi): Sensing vs Intuition",
        "html": f"""
        <div class="h-full flex flex-col">
            {make_header("MODUL 2 • FRAMEWORK MBTI", "Sensing (S) vs Intuition (N)", "Fakta Nyata vs Kemungkinan Masa Depan")}

            <div class="grid grid-cols-2 gap-8 flex-1">
                <!-- Card 1: Sensing (S) -->
                <div class="bg-white p-10 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-6">
                            <div class="flex items-center gap-4">
                                <div class="w-16 h-16 rounded-2xl bg-[#0D1B2A] text-white flex items-center justify-center font-black text-3xl">
                                    S
                                </div>
                                <div>
                                    <h3 class="text-3xl font-extrabold text-[#0D1B2A]">Sensing</h3>
                                    <span class="text-base text-[#64748B] font-bold">Faktual, Rinci, dan Konkret</span>
                                </div>
                            </div>
                            <span class="material-symbols-outlined text-4xl text-emerald-600">search</span>
                        </div>

                        <p class="text-lg text-[#334155] leading-relaxed mb-6 font-medium">
                            Menyerap informasi yang nyata dan aktual (apa yang sedang terjadi sekarang). Sangat cermat terhadap rincian detail dan mengutamakan kegunaan praktis di lapangan kerja.
                        </p>

                        <div class="space-y-4">
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">fact_check</span>
                                <span>Berpijak pada fakta riil, data historis yang jelas, dan bukti empiris.</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">visibility</span>
                                <span>Mengingat detail spesifik dan urutan tahapan kerja dengan sangat akurat.</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">construction</span>
                                <span>Memahami konsep melalui penerapan nyata langsung dalam pekerjaan.</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">history</span>
                                <span>Menghormati prosedur operasional baku (SOP) dan pengalaman teruji.</span>
                            </div>
                        </div>
                    </div>

                    <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 text-sm text-[#475569] font-bold">
                        🎯 <strong>Pertanyaan Kunci:</strong> <em>"Apa data nyatanya dan bagaimana langkah konkret pelaksanaannya hari ini?"</em>
                    </div>
                </div>

                <!-- Card 2: Intuition (N) -->
                <div class="bg-gradient-to-br from-white to-[#EFF6FF] p-10 rounded-[32px] border-2 border-[#4F90F6] shadow-xl flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-6">
                            <div class="flex items-center gap-4">
                                <div class="w-16 h-16 rounded-2xl bg-[#2563EB] text-white flex items-center justify-center font-black text-3xl shadow-md">
                                    N
                                </div>
                                <div>
                                    <h3 class="text-3xl font-extrabold text-[#0D1B2A]">Intuition</h3>
                                    <span class="text-base text-[#1D4ED8] font-bold">Konseptual, Pola, dan Inovasi</span>
                                </div>
                            </div>
                            <span class="material-symbols-outlined text-4xl text-indigo-600">auto_awesome</span>
                        </div>

                        <p class="text-lg text-[#334155] leading-relaxed mb-6 font-medium">
                            Menyerap fakta dengan melihat gambaran menyeluruh <em>(big picture)</em>. Tertarik membaca keterkaitan ide, tren jangka panjang, dan kemungkinan masa depan.
                        </p>

                        <div class="space-y-4">
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">trending_up</span>
                                <span>Berorientasi pada visi masa depan, perubahan tren, dan peluang baru.</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">schema</span>
                                <span>Mencari hubungan antardata dibanding menghafal informasi yang terpisah.</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">lightbulb</span>
                                <span>Kreatif dalam gagasan konseptual dan menyukai pemikiran terobosan.</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">rocket_launch</span>
                                <span>Senang memperjelas arah strategis besar sebelum merinci hal-hal teknis.</span>
                            </div>
                        </div>
                    </div>

                    <div class="p-5 rounded-2xl bg-[#E6F0FD] border border-[#9FBEED] text-sm text-[#1E3A8A] font-bold">
                        🎯 <strong>Pertanyaan Kunci:</strong> <em>"Apa makna di balik tren ini dan terobosan apa yang dapat kita ciptakan?"</em>
                    </div>
                </div>
            </div>
        </div>
        """
    },

    # SLIDE 10: DEEP DIVE T vs F
    {
        "id": 10,
        "category": "MODUL 2: FRAMEWORK MBTI",
        "title": "Dimensi 3 (Keputusan): Thinking vs Feeling",
        "html": f"""
        <div class="h-full flex flex-col">
            {make_header("MODUL 2 • FRAMEWORK MBTI", "Thinking (T) vs Feeling (F)", "Logika Sebab-Akibat vs Nilai Kemanusiaan")}

            <div class="grid grid-cols-2 gap-8 flex-1">
                <!-- Card 1: Thinking (T) -->
                <div class="bg-white p-10 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-6">
                            <div class="flex items-center gap-4">
                                <div class="w-16 h-16 rounded-2xl bg-[#0D1B2A] text-white flex items-center justify-center font-black text-3xl">
                                    T
                                </div>
                                <div>
                                    <h3 class="text-3xl font-extrabold text-[#0D1B2A]">Thinking</h3>
                                    <span class="text-base text-[#64748B] font-bold">Logika Obyektif & Analitis</span>
                                </div>
                            </div>
                            <span class="material-symbols-outlined text-4xl text-cyan-600">gavel</span>
                        </div>

                        <p class="text-lg text-[#334155] leading-relaxed mb-6 font-medium">
                            Menimbang pilihan secara terpisah dari faktor perasaan pribadi. Membedah pro dan kontra secara objektif dengan patokan aturan sebab-akibat yang jelas dan konsisten.
                        </p>

                        <div class="space-y-4">
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">analytics</span>
                                <span>Menggunakan penalaran sebab-akibat yang rasional dan terukur.</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">precision_manufacturing</span>
                                <span>Menyampaikan evaluasi analitis secara lugas demi perbaikan sistem kerja.</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">verified_user</span>
                                <span>Berpegang teguh pada standar kebenaran baku yang adil untuk semua pihak.</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">rule</span>
                                <span>Keadilan diartikan sebagai: <strong>semua pihak diperlakukan dengan aturan baku yang persis sama</strong>.</span>
                            </div>
                        </div>
                    </div>

                    <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 text-sm text-[#475569] font-bold">
                        ⚖️ <strong>Prinsip Berpikir:</strong> <em>"Apakah keputusan ini logis, konsisten, dan memenuhi kaidah efisiensi organisasi?"</em>
                    </div>
                </div>

                <!-- Card 2: Feeling (F) -->
                <div class="bg-gradient-to-br from-white to-[#EFF6FF] p-10 rounded-[32px] border-2 border-[#4F90F6] shadow-xl flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-6">
                            <div class="flex items-center gap-4">
                                <div class="w-16 h-16 rounded-2xl bg-[#2563EB] text-white flex items-center justify-center font-black text-3xl shadow-md">
                                    F
                                </div>
                                <div>
                                    <h3 class="text-3xl font-extrabold text-[#0D1B2A]">Feeling</h3>
                                    <span class="text-base text-[#1D4ED8] font-bold">Nilai Kemanusiaan & Harmoni</span>
                                </div>
                            </div>
                            <span class="material-symbols-outlined text-4xl text-rose-500">favorite</span>
                        </div>

                        <p class="text-lg text-[#334155] leading-relaxed mb-6 font-medium">
                            Mempertimbangkan dampak keputusan terhadap manusia yang terlibat. Menimbang keharmonisan tim, rasa keadilan manusiawi, dan motivasi rekan kerja.
                        </p>

                        <div class="space-y-4">
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">volunteer_activism</span>
                                <span>Peka dan berempati mendalam terhadap situasi serta beban emosional orang lain.</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">sentiment_satisfied</span>
                                <span>Bersemangat saat lingkungan kerja penuh rasa saling mendukung dan menghargai.</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">groups</span>
                                <span>Menjaga agar iklim kerja tetap kondusif dan hubungan antarkaryawan tidak retak.</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">handshake</span>
                                <span>Keadilan diartikan sebagai: <strong>setiap individu diperlakukan sesuai situasi dan kebutuhan uniknya</strong>.</span>
                            </div>
                        </div>
                    </div>

                    <div class="p-5 rounded-2xl bg-[#E6F0FD] border border-[#9FBEED] text-sm text-[#1E3A8A] font-bold">
                        ❤️ <strong>Prinsip Berpikir:</strong> <em>"Bagaimana keputusan ini mempengaruhi keharmonisan tim dan motivasi rekan kerja kita?"</em>
                    </div>
                </div>
            </div>
        </div>
        """
    },

    # SLIDE 11: DEEP DIVE J vs P
    {
        "id": 11,
        "category": "MODUL 2: FRAMEWORK MBTI",
        "title": "Dimensi 4 (Gaya Hidup): Judging vs Perceiving",
        "html": f"""
        <div class="h-full flex flex-col">
            {make_header("MODUL 2 • FRAMEWORK MBTI", "Judging (J) vs Perceiving (P)", "Jadwal Teratur vs Fleksibilitas Spontan")}

            <div class="grid grid-cols-2 gap-8 flex-1">
                <!-- Card 1: Judging (J) -->
                <div class="bg-white p-10 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-6">
                            <div class="flex items-center gap-4">
                                <div class="w-16 h-16 rounded-2xl bg-[#0D1B2A] text-white flex items-center justify-center font-black text-3xl">
                                    J
                                </div>
                                <div>
                                    <h3 class="text-3xl font-extrabold text-[#0D1B2A]">Judging</h3>
                                    <span class="text-base text-[#64748B] font-bold">Teratur, Terjadwal, dan Tertata</span>
                                </div>
                            </div>
                            <span class="material-symbols-outlined text-4xl text-blue-600">checklist</span>
                        </div>

                        <p class="text-lg text-[#334155] leading-relaxed mb-6 font-medium">
                            Menyukai kehidupan kerja yang terencana dan teratur. Berusaha mengelola tugas dengan tahapan yang pasti. Merasa nyaman jika keputusan sudah tuntas diambil dan urusan telah selesai rapi.
                        </p>

                        <div class="space-y-4">
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">event</span>
                                <span>Aktivitas tercatat rapi di dalam agenda dan jadwal kerja tertulis.</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">format_list_numbered</span>
                                <span>Bekerja secara metodis dan menyusun rencana jangka pendek maupun panjang.</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">timer</span>
                                <span>Tidak suka tenggat waktu mepet; berusaha menuntaskan tugas lebih cepat.</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">lock_clock</span>
                                <span>Menyukai kejelasan dan kepastian hasil kerja yang pasti (closure).</span>
                            </div>
                        </div>
                    </div>

                    <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 text-sm text-[#475569] font-bold">
                        📅 <strong>Motto Kerja:</strong> <em>"Rencanakan pekerjaan Anda, lalu tuntaskan sesuai agenda secara disiplin."</em>
                    </div>
                </div>

                <!-- Card 2: Perceiving (P) -->
                <div class="bg-gradient-to-br from-white to-[#EFF6FF] p-10 rounded-[32px] border-2 border-[#4F90F6] shadow-xl flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-6">
                            <div class="flex items-center gap-4">
                                <div class="w-16 h-16 rounded-2xl bg-[#2563EB] text-white flex items-center justify-center font-black text-3xl shadow-md">
                                    P
                                </div>
                                <div>
                                    <h3 class="text-3xl font-extrabold text-[#0D1B2A]">Perceiving</h3>
                                    <span class="text-base text-[#1D4ED8] font-bold">Fleksibel, Spontan, dan Adaptif</span>
                                </div>
                            </div>
                            <span class="material-symbols-outlined text-4xl text-emerald-500">explore</span>
                        </div>

                        <p class="text-lg text-[#334155] leading-relaxed mb-6 font-medium">
                            Menyukai alur kerja yang luwes dan terbuka. Menikmati proses memahami situasi yang dinamis daripada membatasi diri dengan rencana kaku. Menjaga pilihan tetap terbuka untuk peluang baru.
                        </p>

                        <div class="space-y-4">
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">autorenew</span>
                                <span>Cepat menyesuaikan diri terhadap perubahan tak terduga di lapangan.</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">psychology</span>
                                <span>Memiliki kecerdikan tinggi saat harus berimprovisasi mengatasi masalah baru.</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">speed</span>
                                <span>Mampu mengerahkan konsentrasi luar biasa menjelang batas akhir waktu tugas.</span>
                            </div>
                            <div class="flex items-start gap-3.5 text-base text-[#1E293B] font-semibold">
                                <span class="material-symbols-outlined text-[#2563EB] text-2xl mt-0.5">lock_open</span>
                                <span>Nyaman dengan ruang gerak bebas dan senang mengeksplorasi opsi segar.</span>
                            </div>
                        </div>
                    </div>

                    <div class="p-5 rounded-2xl bg-[#E6F0FD] border border-[#9FBEED] text-sm text-[#1E3A8A] font-bold">
                        🌊 <strong>Motto Kerja:</strong> <em>"Tetap tangkas dan responsif mengikuti perubahan kebutuhan di lapangan."</em>
                    </div>
                </div>
            </div>
        </div>
        """
    },

    # SLIDE 12: 16 TIPOLOGI KUADRAN
    {
        "id": 12,
        "category": "MODUL 3: PROFIL TOKOH",
        "title": "Peta 16 Tipe: 4 Kuadran Temperamen",
        "html": f"""
        <div class="h-full flex flex-col">
            {make_header("MODUL 3 • PROFIL TOKOH", "Peta 16 Tipe: 4 Kuadran Karakter Kerja", "Pengelompokan Temperamen")}

            <div class="grid grid-cols-2 gap-8 flex-1">
                <!-- Quadrant 1: NT Rationals -->
                <div class="bg-gradient-to-br from-white to-[#F0F7FF] p-8 rounded-[32px] border-2 border-[#4F90F6]/60 shadow-md flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <span class="px-4 py-1.5 rounded-full bg-[#2563EB] text-white font-black text-sm tracking-wider">
                                KUADRAN NT • RATIONALS
                            </span>
                            <span class="material-symbols-outlined text-3xl text-[#2563EB]">terminal</span>
                        </div>
                        <h3 class="text-2xl font-extrabold text-[#0D1B2A] mb-2">Arsitek Strategi & Sistem</h3>
                        <p class="text-base text-[#475569] font-medium mb-6">Berorientasi pada teori, visi makro, perbaikan efisiensi sistem, dan desain rencana jangka panjang.</p>
                        
                        <div class="grid grid-cols-4 gap-3">
                            <div class="p-4 bg-white rounded-2xl border-2 border-[#9FBEED] text-center shadow-sm">
                                <div class="font-black text-[#2563EB] text-xl">INTJ</div>
                                <div class="text-xs text-[#64748B] font-bold">Architect</div>
                            </div>
                            <div class="p-4 bg-white rounded-2xl border-2 border-[#9FBEED] text-center shadow-sm">
                                <div class="font-black text-[#2563EB] text-xl">INTP</div>
                                <div class="text-xs text-[#64748B] font-bold">Logician</div>
                            </div>
                            <div class="p-4 bg-white rounded-2xl border-2 border-[#9FBEED] text-center shadow-sm">
                                <div class="font-black text-[#2563EB] text-xl">ENTJ</div>
                                <div class="text-xs text-[#64748B] font-bold">Commander</div>
                            </div>
                            <div class="p-4 bg-white rounded-2xl border-2 border-[#9FBEED] text-center shadow-sm">
                                <div class="font-black text-[#2563EB] text-xl">ENTP</div>
                                <div class="text-xs text-[#64748B] font-bold">Debater</div>
                            </div>
                        </div>
                    </div>
                    <div class="text-sm text-[#1E3A8A] font-extrabold pt-4 border-t-2 border-slate-200">
                        ⚡ Nilai Utama: Inovasi logika, penguasaan kompetensi, dan perencanaan masa depan.
                    </div>
                </div>

                <!-- Quadrant 2: NF Idealists -->
                <div class="bg-gradient-to-br from-white to-[#FAF5FF] p-8 rounded-[32px] border-2 border-purple-300 shadow-md flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <span class="px-4 py-1.5 rounded-full bg-purple-700 text-white font-black text-sm tracking-wider">
                                KUADRAN NF • IDEALISTS
                            </span>
                            <span class="material-symbols-outlined text-3xl text-purple-700">volunteer_activism</span>
                        </div>
                        <h3 class="text-2xl font-extrabold text-[#0D1B2A] mb-2">Katalisator Manusia & Nilai</h3>
                        <p class="text-base text-[#475569] font-medium mb-6">Berorientasi pada makna manusia, potensi individu, integritas moral, dan komunikasi persuasif.</p>
                        
                        <div class="grid grid-cols-4 gap-3">
                            <div class="p-4 bg-white rounded-2xl border-2 border-purple-200 text-center shadow-sm">
                                <div class="font-black text-purple-700 text-xl">INFJ</div>
                                <div class="text-xs text-[#64748B] font-bold">Advocate</div>
                            </div>
                            <div class="p-4 bg-white rounded-2xl border-2 border-purple-200 text-center shadow-sm">
                                <div class="font-black text-purple-700 text-xl">INFP</div>
                                <div class="text-xs text-[#64748B] font-bold">Mediator</div>
                            </div>
                            <div class="p-4 bg-white rounded-2xl border-2 border-purple-200 text-center shadow-sm">
                                <div class="font-black text-purple-700 text-xl">ENFJ</div>
                                <div class="text-xs text-[#64748B] font-bold">Protagonist</div>
                            </div>
                            <div class="p-4 bg-white rounded-2xl border-2 border-purple-200 text-center shadow-sm">
                                <div class="font-black text-purple-700 text-xl">ENFP</div>
                                <div class="text-xs text-[#64748B] font-bold">Campaigner</div>
                            </div>
                        </div>
                    </div>
                    <div class="text-sm text-purple-900 font-extrabold pt-4 border-t-2 border-slate-200">
                        ❤️ Nilai Utama: Pengembangan potensi rekan tim, autentisitas, dan misi sosial bernilai luhur.
                    </div>
                </div>

                <!-- Quadrant 3: SJ Guardians -->
                <div class="bg-gradient-to-br from-white to-[#F0FDF4] p-8 rounded-[32px] border-2 border-emerald-300 shadow-md flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <span class="px-4 py-1.5 rounded-full bg-emerald-700 text-white font-black text-sm tracking-wider">
                                KUADRAN SJ • GUARDIANS
                            </span>
                            <span class="material-symbols-outlined text-3xl text-emerald-700">shield</span>
                        </div>
                        <h3 class="text-2xl font-extrabold text-[#0D1B2A] mb-2">Penjaga Stabilitas & Prosedur</h3>
                        <p class="text-base text-[#475569] font-medium mb-6">Berorientasi pada tanggung jawab tinggi, kestabilan organisasi, ketaatan SOP, dan keandalan tugas.</p>
                        
                        <div class="grid grid-cols-4 gap-3">
                            <div class="p-4 bg-white rounded-2xl border-2 border-emerald-200 text-center shadow-sm">
                                <div class="font-black text-emerald-700 text-xl">ISTJ</div>
                                <div class="text-xs text-[#64748B] font-bold">Inspector</div>
                            </div>
                            <div class="p-4 bg-white rounded-2xl border-2 border-emerald-200 text-center shadow-sm">
                                <div class="font-black text-emerald-700 text-xl">ISFJ</div>
                                <div class="text-xs text-[#64748B] font-bold">Defender</div>
                            </div>
                            <div class="p-4 bg-white rounded-2xl border-2 border-emerald-200 text-center shadow-sm">
                                <div class="font-black text-emerald-700 text-xl">ESTJ</div>
                                <div class="text-xs text-[#64748B] font-bold">Executive</div>
                            </div>
                            <div class="p-4 bg-white rounded-2xl border-2 border-emerald-200 text-center shadow-sm">
                                <div class="font-black text-emerald-700 text-xl">ESFJ</div>
                                <div class="text-xs text-[#64748B] font-bold">Consul</div>
                            </div>
                        </div>
                    </div>
                    <div class="text-sm text-emerald-900 font-extrabold pt-4 border-t-2 border-slate-200">
                        🛡️ Nilai Utama: Ketertiban operasional, akurasi administrasi, dan kepastian hasil kerja.
                    </div>
                </div>

                <!-- Quadrant 4: SP Artisans -->
                <div class="bg-gradient-to-br from-white to-[#FFFBEB] p-8 rounded-[32px] border-2 border-amber-300 shadow-md flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <span class="px-4 py-1.5 rounded-full bg-amber-600 text-white font-black text-sm tracking-wider">
                                KUADRAN SP • ARTISANS
                            </span>
                            <span class="material-symbols-outlined text-3xl text-amber-600">speed</span>
                        </div>
                        <h3 class="text-2xl font-extrabold text-[#0D1B2A] mb-2">Taktisi Lapangan & Penuntas Krisis</h3>
                        <p class="text-base text-[#475569] font-medium mb-6">Berorientasi pada tindakan nyata, solusi praktis segera, manuver krisis, dan keluwesan adaptasi.</p>
                        
                        <div class="grid grid-cols-4 gap-3">
                            <div class="p-4 bg-white rounded-2xl border-2 border-amber-200 text-center shadow-sm">
                                <div class="font-black text-amber-700 text-xl">ISTP</div>
                                <div class="text-xs text-[#64748B] font-bold">Virtuoso</div>
                            </div>
                            <div class="p-4 bg-white rounded-2xl border-2 border-amber-200 text-center shadow-sm">
                                <div class="font-black text-amber-700 text-xl">ISFP</div>
                                <div class="text-xs text-[#64748B] font-bold">Adventurer</div>
                            </div>
                            <div class="p-4 bg-white rounded-2xl border-2 border-amber-200 text-center shadow-sm">
                                <div class="font-black text-amber-700 text-xl">ESTP</div>
                                <div class="text-xs text-[#64748B] font-bold">Entrepreneur</div>
                            </div>
                            <div class="p-4 bg-white rounded-2xl border-2 border-amber-200 text-center shadow-sm">
                                <div class="font-black text-amber-700 text-xl">ESFP</div>
                                <div class="text-xs text-[#64748B] font-bold">Entertainer</div>
                            </div>
                        </div>
                    </div>
                    <div class="text-sm text-amber-900 font-extrabold pt-4 border-t-2 border-slate-200">
                        ⚡ Nilai Utama: Kecepatan respon, keberanian bertindak di lapangan, dan hasil praktis instan.
                    </div>
                </div>
            </div>
        </div>
        """
    },

    # SLIDE 13: SPOTLIGHT SJ GUARDIANS
    {
        "id": 13,
        "category": "MODUL 3: PROFIL TOKOH",
        "title": "Profil Tokoh Kuadran SJ (Guardians)",
        "html": f"""
        <div class="h-full flex flex-col">
            {make_header("MODUL 3 • PROFIL TOKOH", "The Guardians: Penjaga Stabilitas & Kepatuhan Prosedur", "ISTJ • ESTJ • ISFJ • ESFJ", "bg-emerald-100 text-emerald-800 border-emerald-300")}

            <!-- 4 Archetype Cards with Linear Gradient Mask Photo & Matched Bullet Alignments -->
            <div class="grid grid-cols-4 gap-6 flex-1">
                {make_archetype_card("ISTJ", "The Inspector", "Basuki Tjahaja P. (Ahok)", img_ahok, [
                    "Praktis, sistematis, dan berpegang teguh pada fakta riil.",
                    "Tanggung jawab & loyalitas kerja terbukti sangat tinggi.",
                    "Konsistensi tinggi menuntaskan tugas tepat waktu."
                ], [
                    "Terpaku kaku pada aturan baku (textbook).",
                    "Sulit mendelegasikan tugas (masalah kepercayaan).",
                    "Kurang mempertimbangkan dampak emosional tim."
                ], "ENFP / ENTP", "bg-emerald-600")}

                {make_archetype_card("ESTJ", "The Executive", "Dahlan Iskan", img_dahlan, [
                    "Sangat piawai mengatur operasional & koordinasi tim.",
                    "Tegas, sangat menghargai efisiensi dan hasil nyata.",
                    "Standar kerja transparan dan disiplin eksekusi."
                ], [
                    "Tidak sabar terhadap yang lambat ikuti prosedur.",
                    "Cenderung mengambil keputusan terlalu cepat/bias.",
                    "Terkesan mendominasi & enggan mendengarkan."
                ], "INFP / ISFP", "bg-emerald-600")}

                {make_archetype_card("ISFJ", "The Defender", "Maudy Ayunda", img_maudy, [
                    "Sangat teliti, kooperatif, dan penuh perhatian.",
                    "Menjaga prosedur kebutuhan operasional rapi.",
                    "Menuntaskan amanah dengan tekun, setia & tenang."
                ], [
                    "Sulit menegaskan batasan kebutuhan pribadi.",
                    "Rawan memendam keluhan hingga tertekan sendiri.",
                    "Merasa cemas saat terjadi perombakan sistem."
                ], "ENTP / ENTJ", "bg-emerald-600")}

                {make_archetype_card("ESFJ", "The Consul", "Maia Estianty", img_maia, [
                    "Hangat, ramah, dan sigap menolong sesama tim.",
                    "Sangat teliti menindaklanjuti detail tugas kerja.",
                    "Menghadirkan rasa aman dan stabilitas dalam tim."
                ], [
                    "Memaksakan keharmonisan ('kita semua harus akur').",
                    "Terlalu sensitif saat menerima evaluasi kritis.",
                    "Meragukan diri bila tidak mendapat pengakuan."
                ], "INTP / INTJ", "bg-emerald-600")}
            </div>
        </div>
        """
    },

    # SLIDE 14: SPOTLIGHT NT RATIONALS
    {
        "id": 14,
        "category": "MODUL 3: PROFIL TOKOH",
        "title": "Profil Tokoh Kuadran NT (Rationals)",
        "html": f"""
        <div class="h-full flex flex-col">
            {make_header("MODUL 3 • PROFIL TOKOH", "The Rationals: Arsitek Strategi & Perancang Sistem", "ENTJ • INTJ • ENTP • INTP", "bg-blue-100 text-blue-800 border-blue-300")}

            <!-- 4 Archetype Cards with Linear Gradient Mask Photo & Matched Bullet Alignments -->
            <div class="grid grid-cols-4 gap-6 flex-1">
                {make_archetype_card("ENTJ", "The Commander", "Prof. B.J. Habibie", img_habibie, [
                    "Pemikir konseptual & pembangun organisasi ulung.",
                    "Menerjemahkan visi besar ke rencana terukur.",
                    "Cepat mengoreksi prosedur yang tidak efisien."
                ], [
                    "Terkesan direktif dan agresif dalam memimpin.",
                    "Kurang memperhatikan kebutuhan emosional tim.",
                    "Tidak sabar terhadap eksekusi detail teknis."
                ], "INFP / ISFJ", "bg-[#2563EB]")}

                {make_archetype_card("INTJ", "The Architect", "Sri Mulyani Indrawati", img_srimulyani, [
                    "Visi jangka panjang dengan ketajaman analisis.",
                    "Mampu merumuskan solusi atas masalah makro rumit.",
                    "Standar integritas logika yang sangat kuat."
                ], [
                    "Cenderung menjadi penyendiri & kritis thd rekan.",
                    "Jarang memberikan pujian verbal kepada tim.",
                    "Sulit menerima data yang di luar polanya."
                ], "ENFP / ESFJ", "bg-[#2563EB]")}

                {make_archetype_card("ENTP", "The Debater", "Tony Stark / Innovator", img_tony, [
                    "Cerdik, kreatif, cepat membaca celah peluang.",
                    "Sangat asertif dan penuh ide-ide inovasi baru.",
                    "Piawai bermanuver dalam situasi ketidakpastian."
                ], [
                    "Cepat bosan terhadap rutinitas eksekusi detail.",
                    "Suka mendebat tanpa menuntaskan solusi final.",
                    "Kurang fokus pada satu sasaran utama."
                ], "INFJ / ISTJ", "bg-[#2563EB]")}

                {make_archetype_card("INTP", "The Logician", "Gus Dur (Abdurrahman W.)", img_gusdur, [
                    "Pemecah masalah orisinal dan sangat mendalam.",
                    "Menemukan inti masalah rumit dari sudut pandang unik.",
                    "Kritis secara mandiri, berani keluar dari pakem."
                ], [
                    "Sering menunda aksi karena terus menganalisis.",
                    "Terkesan sinis bila melihat ketidakkonsistenan.",
                    "Mengabaikan hal-hal praktis dan kebutuhan fisik."
                ], "ENTJ / ESTJ", "bg-[#2563EB]")}
            </div>
        </div>
        """
    },

    # SLIDE 15: SPOTLIGHT NF IDEALISTS
    {
        "id": 15,
        "category": "MODUL 3: PROFIL TOKOH",
        "title": "Profil Tokoh Kuadran NF (Idealists)",
        "html": f"""
        <div class="h-full flex flex-col">
            {make_header("MODUL 3 • PROFIL TOKOH", "The Idealists: Katalisator Manusia & Nilai Organisasi", "ENFJ • INFJ • ENFP • INFP", "bg-purple-100 text-purple-800 border-purple-300")}

            <!-- 4 Archetype Cards with Linear Gradient Mask Photo & Matched Bullet Alignments -->
            <div class="grid grid-cols-4 gap-6 flex-1">
                {make_archetype_card("ENFJ", "The Protagonist", "Sandiaga Uno", img_sandiaga, [
                    "Hangat, suportif, komunikator persuasif ulung.",
                    "Membangun konsensus di antara pihak beragam.",
                    "Menginspirasi tim memunculkan potensi terbaik."
                ], [
                    "Mengambil keputusan terburu demi menjaga harmoni.",
                    "Sangat sensitif bila menghadapi kritik keras.",
                    "Mengabaikan data bila bertabrakan dengan relasi."
                ], "INTP / ISTP", "bg-purple-700")}

                {make_archetype_card("INFJ", "The Advocate", "Najwa Shihab", img_najwa, [
                    "Visioner, idealis mendalam, berintegritas tinggi.",
                    "Membaca motivasi tersembunyi dengan tepat.",
                    "Berkomitmen kuat pada misi perbaikan bersama."
                ], [
                    "Sangat teguh mempertahankan visinya tanpa kompromi.",
                    "Terkesan misterius atau sulit ditebak oleh tim.",
                    "Rentan mengalami kelelahan emosional (burnout)."
                ], "ENTP / ESTP", "bg-purple-700")}

                {make_archetype_card("ENFP", "The Campaigner", "Enzy Storia", img_enzy, [
                    "Sangat antusias, kreatif, energik, dan optimis.",
                    "Mudah menjalin kedekatan emosional hangat.",
                    "Mendorong rekan kerja untuk terus bertumbuh."
                ], [
                    "Perhatian mudah terpecah oleh ide-ide baru.",
                    "Sering menyepelekan detail teknis dan deadline.",
                    "Sulit menolak ajakan atau proyek tambahan."
                ], "INTJ / ISTJ", "bg-purple-700")}

                {make_archetype_card("INFP", "The Mediator", "Iwan Fals", img_iwan, [
                    "Idealis, setia pada nilai moral batiniah.",
                    "Empati sangat dalam terhadap sesama rekan kerja.",
                    "Kreativitas bernilai filosofis dan bermakna."
                ], [
                    "Menarik diri bila terjadi konflik terbuka keras.",
                    "Sulit mengurai nilai luhur ke rencana aksi teknis.",
                    "Mudah berkecil hati jika kenyataan meleset."
                ], "ENTJ / ESTJ", "bg-purple-700")}
            </div>
        </div>
        """
    },

    # SLIDE 16: SPOTLIGHT SP ARTISANS
    {
        "id": 16,
        "category": "MODUL 3: PROFIL TOKOH",
        "title": "Profil Tokoh Kuadran SP (Artisans)",
        "html": f"""
        <div class="h-full flex flex-col">
            {make_header("MODUL 3 • PROFIL TOKOH", "The Artisans: Taktisi Lapangan & Penuntas Krisis Sigap", "ISTP • ESTP • ESFP • ISFP", "bg-amber-100 text-amber-900 border-amber-300")}

            <!-- 4 Archetype Cards with Linear Gradient Mask Photo & Matched Bullet Alignments -->
            <div class="grid grid-cols-4 gap-6 flex-1">
                {make_archetype_card("ISTP", "The Virtuoso", "Steve Jobs (Craftsman)", img_jobs, [
                    "Faktual, praktis, analisis teknis sangat jitu.",
                    "Bergerak cepat menembus inti permasalahan.",
                    "Mencapai efisiensi maksimal dengan usaha terarah."
                ], [
                    "Kurang peka terhadap kebutuhan emosional tim.",
                    "Sinis terhadap teori abstrak tanpa aplikasi instan.",
                    "Terlalu fokus pada hasil jangka pendek."
                ], "ENFJ / ESFJ", "bg-amber-600")}

                {make_archetype_card("ESTP", "The Entrepreneur", "Deddy Corbuzier", img_deddy, [
                    "Pengamat sigap, pemecah masalah realistis.",
                    "Merespon kreatif situasi lapangan darurat.",
                    "Banyak akal mencairkan kebuntuan tim."
                ], [
                    "Menolak struktur kaku dan jadwal birokratis.",
                    "Terjebak dalam aksi tanpa rencana matang.",
                    "Kurang peka terhadap perasaan halus rekan."
                ], "INFJ / ISFJ", "bg-amber-600")}

                {make_archetype_card("ESFP", "The Entertainer", "Raffi Ahmad", img_raffi, [
                    "Sangat persuasif, murah hati, dan optimis.",
                    "Pemain tim ulung, mencairkan ketegangan.",
                    "Menuntaskan tugas dengan suasana gembira."
                ], [
                    "Bertindak impulsif dan enggan analisis rumit.",
                    "Terlalu mengejar kenyamanan sesaat.",
                    "Mengabaikan dampak jangka panjang."
                ], "INTJ / ISTJ", "bg-amber-600")}

                {make_archetype_card("ISFP", "The Adventurer", "Agus H. Yudhoyono (AHY)", img_ahy, [
                    "Sangat peka, tenang, teguh pada komitmen.",
                    "Bertindak selaras dengan nilai integritas pribadi.",
                    "Eksekutor karya lapangan yang rapi dan praktis."
                ], [
                    "Menghindari perdebatan keras secara langsung.",
                    "Kurang nyaman dengan aturan birokrasi kaku.",
                    "Ragu menyuarakan kritik saat rapat resmi."
                ], "ENTJ / ESTJ", "bg-amber-600")}
            </div>
        </div>
        """
    },

    # SLIDE 17: MASTER MATRIX PERBANDINGAN
    {
        "id": 17,
        "category": "MODUL 3: PROFIL TOKOH",
        "title": "Matriks Perbandingan 4 Temperamen",
        "html": f"""
        <div class="h-full flex flex-col">
            {make_header("MODUL 3 • PROFIL TOKOH", "Matriks Perbandingan Utama: Fokus Kerja, Stres & Apresiasi", "Ringkasan 4 Kuadran")}

            <div class="grid grid-cols-4 gap-6 flex-1">
                <!-- Col 1: SJ Guardians -->
                <div class="bg-white p-7 rounded-[28px] border-2 border-emerald-300 shadow-md flex flex-col justify-between">
                    <div>
                        <div class="flex items-center gap-2.5 mb-5 pb-3 border-b-2 border-slate-100">
                            <span class="material-symbols-outlined text-emerald-700 text-2xl">shield</span>
                            <span class="font-black text-emerald-800 text-xl">SJ GUARDIANS</span>
                        </div>

                        <div class="space-y-5">
                            <div>
                                <div class="text-xs uppercase font-black text-[#64748B]">Fokus Utama di Tempat Kerja</div>
                                <div class="text-base font-bold text-[#0D1B2A] mt-1 leading-snug">Kepatuhan prosedur (SOP), jadwal tertib, disiplin tugas, & stabilitas aset.</div>
                            </div>

                            <div>
                                <div class="text-xs uppercase font-black text-[#64748B]">Reaksi Saat Stres Tinggi</div>
                                <div class="text-base font-bold text-rose-700 mt-1 leading-snug">Menjadi sangat kaku, mencemaskan hal terburuk, & sulit mendelegasikan tugas.</div>
                            </div>

                            <div>
                                <div class="text-xs uppercase font-black text-[#64748B]">Bentuk Apresiasi yang Dibutuhkan</div>
                                <div class="text-base font-semibold text-[#334155] mt-1 leading-snug">Diakui ketelitiannya, kesetiaannya menjaga aturan, dan ketepatan waktunya.</div>
                            </div>
                        </div>
                    </div>
                    <div class="p-4 bg-emerald-50 rounded-2xl text-xs text-emerald-900 font-extrabold border border-emerald-200">
                        📌 Cocok di Bidang: Operasional, Keuangan, Risk Management, Audit & Legal.
                    </div>
                </div>

                <!-- Col 2: NT Rationals -->
                <div class="bg-white p-7 rounded-[28px] border-2 border-[#4F90F6] shadow-md flex flex-col justify-between">
                    <div>
                        <div class="flex items-center gap-2.5 mb-5 pb-3 border-b-2 border-slate-100">
                            <span class="material-symbols-outlined text-[#2563EB] text-2xl">terminal</span>
                            <span class="font-black text-[#2563EB] text-xl">NT RATIONALS</span>
                        </div>

                        <div class="space-y-5">
                            <div>
                                <div class="text-xs uppercase font-black text-[#64748B]">Fokus Utama di Tempat Kerja</div>
                                <div class="text-base font-bold text-[#0D1B2A] mt-1 leading-snug">Desain strategi makro, efisiensi arsitektur kerja, & inovasi pemikiran.</div>
                            </div>

                            <div>
                                <div class="text-xs uppercase font-black text-[#64748B]">Reaksi Saat Stres Tinggi</div>
                                <div class="text-base font-bold text-rose-700 mt-1 leading-snug">Menjadi sinis, terobsesi mengkritik kesalahan orang, & enggan berkompromi.</div>
                            </div>

                            <div>
                                <div class="text-xs uppercase font-black text-[#64748B]">Bentuk Apresiasi yang Dibutuhkan</div>
                                <div class="text-base font-semibold text-[#334155] mt-1 leading-snug">Dihormati keahlian logikanya & diberi otonomi mandiri memecahkan masalah.</div>
                            </div>
                        </div>
                    </div>
                    <div class="p-4 bg-[#EFF6FF] rounded-2xl text-xs text-[#1E40AF] font-extrabold border border-[#9FBEED]">
                        📌 Cocok di Bidang: Corporate Planning, Strategi Bisnis, IT & Litbang.
                    </div>
                </div>

                <!-- Col 3: NF Idealists -->
                <div class="bg-white p-7 rounded-[28px] border-2 border-purple-300 shadow-md flex flex-col justify-between">
                    <div>
                        <div class="flex items-center gap-2.5 mb-5 pb-3 border-b-2 border-slate-100">
                            <span class="material-symbols-outlined text-purple-700 text-2xl">volunteer_activism</span>
                            <span class="font-black text-purple-800 text-xl">NF IDEALISTS</span>
                        </div>

                        <div class="space-y-5">
                            <div>
                                <div class="text-xs uppercase font-black text-[#64748B]">Fokus Utama di Tempat Kerja</div>
                                <div class="text-base font-bold text-[#0D1B2A] mt-1 leading-snug">Budaya kerja sehat, pembinaan insan tim, misi luhur, & integritas moral.</div>
                            </div>

                            <div>
                                <div class="text-xs uppercase font-black text-[#64748B]">Reaksi Saat Stres Tinggi</div>
                                <div class="text-base font-bold text-rose-700 mt-1 leading-snug">Menarik diri dalam kesedihan, merasa diserang secara personal, & putus asa.</div>
                            </div>

                            <div>
                                <div class="text-xs uppercase font-black text-[#64748B]">Bentuk Apresiasi yang Dibutuhkan</div>
                                <div class="text-base font-semibold text-[#334155] mt-1 leading-snug">Diakui ketulusan kontribusinya & didukung gagasannya yang memanusiakan tim.</div>
                            </div>
                        </div>
                    </div>
                    <div class="p-4 bg-purple-50 rounded-2xl text-xs text-purple-900 font-extrabold border border-purple-200">
                        📌 Cocok di Bidang: SDM / Human Capital, Internal Communication, CSR & Budaya.
                    </div>
                </div>

                <!-- Col 4: SP Artisans -->
                <div class="bg-white p-7 rounded-[28px] border-2 border-amber-300 shadow-md flex flex-col justify-between">
                    <div>
                        <div class="flex items-center gap-2.5 mb-5 pb-3 border-b-2 border-slate-100">
                            <span class="material-symbols-outlined text-amber-700 text-2xl">speed</span>
                            <span class="font-black text-amber-800 text-xl">SP ARTISANS</span>
                        </div>

                        <div class="space-y-5">
                            <div>
                                <div class="text-xs uppercase font-black text-[#64748B]">Fokus Utama di Tempat Kerja</div>
                                <div class="text-base font-bold text-[#0D1B2A] mt-1 leading-snug">Aksi nyata di lapangan, kelincahan manuver, penanganan krisis taktis segera.</div>
                            </div>

                            <div>
                                <div class="text-xs uppercase font-black text-[#64748B]">Reaksi Saat Stres Tinggi</div>
                                <div class="text-base font-bold text-rose-700 mt-1 leading-snug">Bertindak tergesa-gesa tanpa pertimbangan, menabrak batas aturan demi solusi instan.</div>
                            </div>

                            <div>
                                <div class="text-xs uppercase font-black text-[#64748B]">Bentuk Apresiasi yang Dibutuhkan</div>
                                <div class="text-base font-semibold text-[#334155] mt-1 leading-snug">Diberi keleluasaan bergerak & dipuji atas respon cepatnya mengatasi hambatan.</div>
                            </div>
                        </div>
                    </div>
                    <div class="p-4 bg-amber-50 rounded-2xl text-xs text-amber-900 font-extrabold border border-amber-200">
                        📌 Cocok di Bidang: Lapangan / Project Site, Pemasaran, Crisis Handling & Event.
                    </div>
                </div>
            </div>
        </div>
        """
    },

    # SLIDE 18: MATRIKS GESEKAN TIPE BERTOLAK BELAKANG
    {
        "id": 18,
        "category": "MODUL 4: SINERGI & PANDUAN PIMPINAN",
        "title": "Akar Gesekan: Bahasa (Words) × Sarana (Tools)",
        "html": f"""
        <div class="h-full flex flex-col">
            {make_header("MODUL 4 • SINERGI & PANDUAN PIMPINAN", "Bagaimana Jika Tipe Bertolak Belakang?", "Words × Tools Clash", "bg-rose-50 text-rose-700 border-rose-200")}

            <div class="grid grid-cols-12 gap-8 flex-1">
                <!-- Left 8 cols: 2x2 Keirsey Cross -->
                <div class="col-span-8 bg-white p-9 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between">
                    <div class="flex items-center justify-between mb-4">
                        <div class="font-black text-[#0D1B2A] text-2xl">Matriks Bahasa (Words) × Sarana Kerja (Tools)</div>
                        <div class="text-sm font-bold text-[#64748B]">Sumbu Komunikasi dan Eksekusi</div>
                    </div>

                    <div class="grid grid-cols-2 gap-5 flex-1">
                        <!-- Top-Left: NF Cooperator -->
                        <div class="p-6 rounded-2xl bg-purple-50 border-2 border-purple-200 flex flex-col justify-between">
                            <div>
                                <div class="flex items-center justify-between mb-2">
                                    <span class="font-black text-purple-900 text-xl">NF Idealists</span>
                                    <span class="text-xs font-black px-3 py-1 rounded-md bg-purple-200 text-purple-900">Abstrak + Kooperatif</span>
                                </div>
                                <p class="text-sm text-[#475569] font-semibold leading-relaxed">Fokus pada Hubungan Baik, Diplomasi, Makna Luhur, & Pertumbuhan Insan.</p>
                            </div>
                            <div class="text-xs font-black text-rose-700 mt-3 flex items-center gap-1.5 p-2 bg-rose-50 rounded-lg">
                                <span class="material-symbols-outlined text-base">sync_alt</span> Rawan bentrok dengan: <strong>SP Artisans</strong>
                            </div>
                        </div>

                        <!-- Top-Right: SJ Cooperator -->
                        <div class="p-6 rounded-2xl bg-emerald-50 border-2 border-emerald-200 flex flex-col justify-between">
                            <div>
                                <div class="flex items-center justify-between mb-2">
                                    <span class="font-black text-emerald-900 text-xl">SJ Guardians</span>
                                    <span class="text-xs font-black px-3 py-1 rounded-md bg-emerald-200 text-emerald-900">Konkret + Kooperatif</span>
                                </div>
                                <p class="text-sm text-[#475569] font-semibold leading-relaxed">Fokus pada Logistik, Administrasi, Stabilitas, & Kepatuhan Prosedur Baku.</p>
                            </div>
                            <div class="text-xs font-black text-rose-700 mt-3 flex items-center gap-1.5 p-2 bg-rose-50 rounded-lg">
                                <span class="material-symbols-outlined text-base">sync_alt</span> Rawan bentrok dengan: <strong>NT Rationals</strong>
                            </div>
                        </div>

                        <!-- Bottom-Left: NT Utilitarian -->
                        <div class="p-6 rounded-2xl bg-blue-50 border-2 border-blue-200 flex flex-col justify-between">
                            <div>
                                <div class="flex items-center justify-between mb-2">
                                    <span class="font-black text-[#1E40AF] text-xl">NT Rationals</span>
                                    <span class="text-xs font-black px-3 py-1 rounded-md bg-[#4F90F6]/25 text-[#1E40AF]">Abstrak + Utilitarian</span>
                                </div>
                                <p class="text-sm text-[#475569] font-semibold leading-relaxed">Fokus pada Strategi, Efisiensi Sistem, Desain Logika Baru, & Kemajuan.</p>
                            </div>
                            <div class="text-xs font-black text-rose-700 mt-3 flex items-center gap-1.5 p-2 bg-rose-50 rounded-lg">
                                <span class="material-symbols-outlined text-base">sync_alt</span> Rawan bentrok dengan: <strong>SJ Guardians</strong>
                            </div>
                        </div>

                        <!-- Bottom-Right: SP Utilitarian -->
                        <div class="p-5 rounded-2xl bg-amber-50 border-2 border-amber-200 flex flex-col justify-between">
                            <div>
                                <div class="flex items-center justify-between mb-2">
                                    <span class="font-black text-amber-900 text-xl">SP Artisans</span>
                                    <span class="text-xs font-black px-3 py-1 rounded-md bg-amber-200 text-amber-900">Konkret + Utilitarian</span>
                                </div>
                                <p class="text-sm text-[#475569] font-semibold leading-relaxed">Fokus pada Taktik Cepat, Aksi Nyata, Kebebasan Berkreasi, & Hasil Instan.</p>
                            </div>
                            <div class="text-xs font-black text-rose-700 mt-3 flex items-center gap-1.5 p-2 bg-rose-50 rounded-lg">
                                <span class="material-symbols-outlined text-base">sync_alt</span> Rawan bentrok dengan: <strong>NF Idealists</strong>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right 4 cols: Clash Root Causes -->
                <div class="col-span-4 flex flex-col gap-5">
                    <div class="bg-gradient-to-br from-[#EFF6FF] via-[#E2EEFE] to-[#D5E6FC] p-8 rounded-[32px] border-2 border-[#9FBEED] flex-1 flex flex-col justify-between">
                        <div>
                            <div class="w-14 h-14 rounded-2xl bg-[#2563EB] text-white flex items-center justify-center mb-4 shadow-md">
                                <span class="material-symbols-outlined text-3xl">compare_arrows</span>
                            </div>
                            <h4 class="font-black text-[#0D1B2A] text-2xl mb-3">Mengapa Gesekan Terjadi?</h4>
                            <div class="space-y-4 text-sm text-[#1E293B] leading-relaxed font-semibold">
                                <div class="p-4 bg-white/90 rounded-2xl border border-white shadow-sm">
                                    <strong class="text-rose-700">SP vs NF (Beda Bahasa):</strong> SP menganggap NF "terlalu banyak teori dan berlebihan", sedangkan NF memandang SP "kurang peduli makna dan dangkal".
                                </div>
                                <div class="p-4 bg-white/90 rounded-2xl border border-white shadow-sm">
                                    <strong class="text-rose-700">NT vs SJ (Beda Metode):</strong> NT menganggap SJ "kaku dan lamban berinovasi", sedangkan SJ menilai NT "terlalu ceroboh dan mengabaikan SOP".
                                </div>
                            </div>
                        </div>
                        <div class="text-sm font-black text-[#1E3A8A] p-3 bg-white/60 rounded-xl text-center">
                            💡 Kuncinya: Terjemahkan arahan ke dalam bahasa kognitif lawan bicara Anda.
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
    },

    # SLIDE 19: ARSITEKTUR SINERGI LEADER & TIM
    {
        "id": 19,
        "category": "MODUL 4: SINERGI & PANDUAN PIMPINAN",
        "title": "Sinergi Terbaik: Pola Pasangan Leader & Tim",
        "html": f"""
        <div class="h-full flex flex-col">
            {make_header("MODUL 4 • SINERGI & PANDUAN PIMPINAN", "Best Team Work: Arsitektur Pasangan Leader & Tim", "Formasi Kerja Juara")}

            <div class="grid grid-cols-2 gap-8 flex-1">
                <!-- Case 1: Leader NF -->
                <div class="bg-white p-8 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between hover:border-[#4F90F6] transition-all">
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <div class="flex items-center gap-3">
                                <span class="px-4 py-1.5 rounded-xl bg-purple-700 text-white font-black text-base">Leader: NF</span>
                                <span class="text-sm font-bold text-[#64748B]">Visionary Inspirer</span>
                            </div>
                            <span class="material-symbols-outlined text-purple-700 text-3xl">supervisor_account</span>
                        </div>
                        <div class="flex items-center gap-3 mb-4">
                            <span class="text-sm font-bold text-[#0D1B2A]">Tim Pendamping Terbaik:</span>
                            <span class="px-3 py-1 rounded-lg bg-emerald-100 text-emerald-800 font-black text-sm">SJ</span>
                            <span class="text-sm font-bold text-slate-400">+</span>
                            <span class="px-3 py-1 rounded-lg bg-blue-100 text-blue-800 font-black text-sm">NT</span>
                        </div>
                        <p class="text-base text-[#334155] font-medium leading-relaxed">
                            Leader NF menginspirasi visi misi dan menjaga komitmen anggota. <strong>SJ</strong> memastikan jadwal, administrasi, dan SOP terlaksana ketat, sementara <strong>NT</strong> menguji kelayakan logika strategi dan sistem.
                        </p>
                    </div>
                    <div class="pt-4 border-t-2 border-slate-100 text-sm text-[#2563EB] font-bold">
                        Hasil: Visi yang menginspirasi berhasil dieksekusi tanpa kebocoran operasional.
                    </div>
                </div>

                <!-- Case 2: Leader SJ -->
                <div class="bg-white p-8 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between hover:border-[#4F90F6] transition-all">
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <div class="flex items-center gap-3">
                                <span class="px-4 py-1.5 rounded-xl bg-emerald-700 text-white font-black text-base">Leader: SJ</span>
                                <span class="text-sm font-bold text-[#64748B]">Operational Commander</span>
                            </div>
                            <span class="material-symbols-outlined text-emerald-700 text-3xl">account_balance</span>
                        </div>
                        <div class="flex items-center gap-3 mb-4">
                            <span class="text-sm font-bold text-[#0D1B2A]">Tim Pendamping Terbaik:</span>
                            <span class="px-3 py-1 rounded-lg bg-amber-100 text-amber-800 font-black text-sm">SP</span>
                            <span class="text-sm font-bold text-slate-400">+</span>
                            <span class="px-3 py-1 rounded-lg bg-purple-100 text-purple-800 font-black text-sm">NF</span>
                        </div>
                        <p class="text-base text-[#334155] font-medium leading-relaxed">
                            Leader SJ menjaga tata kelola dan disiplin organisasi yang kokoh. <strong>SP</strong> memberikan kelincahan mengatasi hambatan teknis mendadak di lapangan, sedangkan <strong>NF</strong> menjaga keharmonisan hubungan dan moral kerja.
                        </p>
                    </div>
                    <div class="pt-4 border-t-2 border-slate-100 text-sm text-emerald-800 font-bold">
                        Hasil: Disiplin operasional tinggi dengan kelincahan lapangan & suasana kerja hangat.
                    </div>
                </div>

                <!-- Case 3: Leader NT -->
                <div class="bg-white p-8 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between hover:border-[#4F90F6] transition-all">
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <div class="flex items-center gap-3">
                                <span class="px-4 py-1.5 rounded-xl bg-[#2563EB] text-white font-black text-base">Leader: NT</span>
                                <span class="text-sm font-bold text-[#64748B]">Strategic Architect</span>
                            </div>
                            <span class="material-symbols-outlined text-[#2563EB] text-3xl">insights</span>
                        </div>
                        <div class="flex items-center gap-3 mb-4">
                            <span class="text-sm font-bold text-[#0D1B2A]">Tim Pendamping Terbaik:</span>
                            <span class="px-3 py-1 rounded-lg bg-purple-100 text-purple-800 font-black text-sm">NF</span>
                            <span class="text-sm font-bold text-slate-400">+</span>
                            <span class="px-3 py-1 rounded-lg bg-amber-100 text-amber-800 font-black text-sm">SP</span>
                        </div>
                        <p class="text-base text-[#334155] font-medium leading-relaxed">
                            Leader NT merancang model kerja dan arsitektur pemecahan masalah rumit. <strong>NF</strong> menerjemahkan strategi menjadi pesan yang memotivasi manusia, sedangkan <strong>SP</strong> langsung melakukan uji coba prototipe ke lapangan nyata.
                        </p>
                    </div>
                    <div class="pt-4 border-t-2 border-slate-100 text-sm text-[#1E40AF] font-bold">
                        Hasil: Strategi berkelas dunia yang membumi secara manusiawi dan cepat teruji.
                    </div>
                </div>

                <!-- Case 4: Leader SP -->
                <div class="bg-white p-8 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between hover:border-[#4F90F6] transition-all">
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <div class="flex items-center gap-3">
                                <span class="px-4 py-1.5 rounded-xl bg-amber-600 text-white font-black text-base">Leader: SP</span>
                                <span class="text-sm font-bold text-[#64748B]">Tactical General</span>
                            </div>
                            <span class="material-symbols-outlined text-amber-600 text-3xl">bolt</span>
                        </div>
                        <div class="flex items-center gap-3 mb-4">
                            <span class="text-sm font-bold text-[#0D1B2A]">Tim Pendamping Terbaik:</span>
                            <span class="px-3 py-1 rounded-lg bg-blue-100 text-blue-800 font-black text-sm">NT</span>
                            <span class="text-sm font-bold text-slate-400">+</span>
                            <span class="px-3 py-1 rounded-lg bg-emerald-100 text-emerald-800 font-black text-sm">SJ</span>
                        </div>
                        <p class="text-base text-[#334155] font-medium leading-relaxed">
                            Leader SP memimpin di garis depan saat krisis dengan keberanian tinggi. <strong>NT</strong> memberikan peta navigasi jangka panjang agar manuver tidak salah arah, dan <strong>SJ</strong> mengamankan dokumentasi serta akuntabilitas aset.
                        </p>
                    </div>
                    <div class="pt-4 border-t-2 border-slate-100 text-sm text-amber-800 font-bold">
                        Hasil: Eksekusi lapangan yang lincah namun tetap terarah dan aman dari risiko regulasi.
                    </div>
                </div>
            </div>
        </div>
        """
    },

    # SLIDE 20: PANDUAN PRAKTIS MANAGER
    {
        "id": 20,
        "category": "MODUL 4: SINERGI & PANDUAN PIMPINAN",
        "title": "Panduan Praktis Manager: Memimpin Tim Berlawanan",
        "html": f"""
        <div class="h-full flex flex-col">
            {make_header("MODUL 4 • SINERGI & PANDUAN PIMPINAN", "Kepribadian Manager Bertolak Belakang dengan Tim", "4 Prinsip Emas Pimpinan")}

            <div class="grid grid-cols-4 gap-6 flex-1">
                <!-- Principle 1 -->
                <div class="bg-white p-8 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between">
                    <div>
                        <div class="w-16 h-16 rounded-2xl bg-[#4F90F6]/15 text-[#2563EB] flex items-center justify-center font-black text-2xl mb-5">
                            01
                        </div>
                        <h3 class="text-2xl font-extrabold text-[#0D1B2A] mb-3">Tidak Ada yang Superior</h3>
                        <p class="text-base text-[#334155] leading-relaxed mb-4 font-semibold">
                            <strong>Tidak ada kepribadian yang "jelek" atau "superior".</strong> Semuanya saling melengkapi dan membawa fungsi penting bagi organisasi.
                        </p>
                        <p class="text-sm text-[#64748B] leading-relaxed font-medium">
                            Tim yang anggotanya berpikir seragam justru berisiko mengalami kebutaan kolektif terhadap ancaman baru.
                        </p>
                    </div>
                    <div class="p-3.5 bg-slate-50 rounded-xl text-sm text-[#0D1B2A] font-extrabold flex items-center gap-2">
                        <span class="material-symbols-outlined text-lg text-[#2563EB]">check</span>
                        Saling Menghargai Peran
                    </div>
                </div>

                <!-- Principle 2 -->
                <div class="bg-white p-8 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between">
                    <div>
                        <div class="w-16 h-16 rounded-2xl bg-[#4F90F6]/15 text-[#2563EB] flex items-center justify-center font-black text-2xl mb-5">
                            02
                        </div>
                        <h3 class="text-2xl font-extrabold text-[#0D1B2A] mb-3">Pahami Diri Terlebih Dahulu</h3>
                        <p class="text-base text-[#334155] leading-relaxed mb-4 font-semibold">
                            <strong>Kenali kelemahan diri sendiri terlebih dahulu</strong>, sebelum menuntut pengertian penuh dari bawahan atau anggota tim Anda.
                        </p>
                        <p class="text-sm text-[#64748B] leading-relaxed font-medium">
                            Ketahui preferensi Anda: apakah cara bicara Anda yang terlalu terburu-buru atau terlalu kritis yang membuat bawahan defensif?
                        </p>
                    </div>
                    <div class="p-3.5 bg-slate-50 rounded-xl text-sm text-[#0D1B2A] font-extrabold flex items-center gap-2">
                        <span class="material-symbols-outlined text-lg text-[#2563EB]">self_improvement</span>
                        Refleksi Diri (Self-Awareness)
                    </div>
                </div>

                <!-- Principle 3 -->
                <div class="bg-white p-8 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between">
                    <div>
                        <div class="w-16 h-16 rounded-2xl bg-[#4F90F6]/15 text-[#2563EB] flex items-center justify-center font-black text-2xl mb-5">
                            03
                        </div>
                        <h3 class="text-2xl font-extrabold text-[#0D1B2A] mb-3">Menghargai Perbedaan</h3>
                        <p class="text-base text-[#334155] leading-relaxed mb-4 font-semibold">
                            <strong>Hargai keunikan tiap orang.</strong> Berhentilah berusaha mengubah bawahan agar menjadi salinan kepribadian Anda.
                        </p>
                        <p class="text-sm text-[#64748B] leading-relaxed font-medium">
                            Tugaskan bawahan pada peran yang memanfaatkan kelebihan alamiahnya, bukan terus mempermasalahkan kelemahannya.
                        </p>
                    </div>
                    <div class="p-3.5 bg-slate-50 rounded-xl text-sm text-[#0D1B2A] font-extrabold flex items-center gap-2">
                        <span class="material-symbols-outlined text-lg text-[#2563EB]">diversity_1</span>
                        Empati Kognitif
                    </div>
                </div>

                <!-- Principle 4 (Featured Clear Stream) -->
                <div class="bg-gradient-to-br from-[#4F90F6] via-[#2563EB] to-[#1D4ED8] p-8 rounded-[32px] text-white shadow-2xl flex flex-col justify-between">
                    <div>
                        <div class="w-16 h-16 rounded-2xl bg-white/20 text-white flex items-center justify-center font-black text-2xl mb-5">
                            04
                        </div>
                        <h3 class="text-2xl font-extrabold mb-3">The Platinum Rule</h3>
                        <p class="text-base text-white/95 leading-relaxed mb-4 font-semibold">
                            <em>"Treat them like what they should be treated."</em>
                        </p>
                        <p class="text-sm text-white/90 leading-relaxed font-medium">
                            Bukan memperlakukan orang lain sebagaimana <strong>Anda</strong> ingin diperlakukan, melainkan perlakukan mereka sebagaimana <strong>mereka butuh</strong> diperlakukan agar potensinya berkembang.
                        </p>
                    </div>
                    <div class="p-3.5 bg-white/20 backdrop-blur rounded-xl text-sm text-white font-black flex items-center gap-2">
                        <span class="material-symbols-outlined text-lg">psychology</span>
                        Kepemimpinan Situasional
                    </div>
                </div>
            </div>
        </div>
        """
    },

    # SLIDE 21: SINTESIS FILOSOFIS & QUOTE LAO TZU
    {
        "id": 21,
        "category": "MODUL 4: SINERGI & PANDUAN PIMPINAN",
        "title": "Sintesis Filosofis: Mengenali Diri & Orang Lain",
        "html": f"""
        <div class="h-full flex flex-col">
            {make_header("MODUL 4 • SINERGI & PANDUAN PIMPINAN", "Sintesis Filosofis: Mengenali Diri dan Memimpin Orang Lain", "Lao Tzu Teaching")}

            <div class="grid grid-cols-12 gap-8 flex-1">
                <!-- Hero Quote Card (6 cols) -->
                <div class="col-span-6 bg-gradient-to-br from-[#4F90F6] via-[#2563EB] to-[#1D4ED8] p-12 rounded-[32px] text-white shadow-2xl flex flex-col justify-between relative overflow-hidden">
                    <div class="absolute -right-8 -top-8 text-white/10 select-none pointer-events-none">
                        <span class="material-symbols-outlined text-[200px]">format_quote</span>
                    </div>

                    <div>
                        <div class="w-16 h-16 rounded-2xl bg-white/20 backdrop-blur-md flex items-center justify-center mb-8">
                            <span class="material-symbols-outlined text-4xl">psychology</span>
                        </div>
                        <blockquote class="text-3xl font-black leading-snug tracking-tight mb-8">
                            “Knowing others is intelligence; knowing yourself is true wisdom.<br/><br/>
                            Mastering others is strength; mastering yourself is true power.”
                        </blockquote>
                        <div class="p-4 bg-white/15 backdrop-blur rounded-2xl text-base text-white/95 font-semibold leading-relaxed">
                            <em>"Mengenali orang lain adalah kecerdasan; mengenali diri sendiri adalah kebijaksanaan sejati. Menguasai orang lain adalah kekuatan; menguasai diri sendiri adalah kekuasaan hakiki."</em>
                        </div>
                    </div>

                    <div class="pt-6 border-t border-white/25 flex items-center justify-between">
                        <div>
                            <div class="text-2xl font-black">Lao Tzu</div>
                            <div class="text-sm text-white/80 font-medium">Filsuf Klasik & Penulis Tao Te Ching</div>
                        </div>
                        <span class="px-4 py-1.5 rounded-full bg-white/20 text-white text-sm font-extrabold">Landasan Kepemimpinan</span>
                    </div>
                </div>

                <!-- 3 Action Pillars Right (6 cols) -->
                <div class="col-span-6 flex flex-col gap-5">
                    <!-- Pillar 1 -->
                    <div class="p-7 bg-white rounded-[28px] border-2 border-slate-200 shadow-md flex items-start gap-5 flex-1">
                        <div class="w-16 h-16 rounded-2xl bg-[#4F90F6]/15 text-[#2563EB] flex items-center justify-center flex-shrink-0">
                            <span class="material-symbols-outlined text-3xl">person_search</span>
                        </div>
                        <div>
                            <div class="font-black text-[#0D1B2A] text-xl mb-1.5">1. Kenali Diri Anda (Know Yourself)</div>
                            <p class="text-base text-[#475569] leading-relaxed font-semibold">
                                Kejujuran mengakui keterbatasan dan titik buta pribadi. Sadari kapan kekuatan alami Anda justru bisa menekan rekan kerja jika dipaksakan berlebihan.
                            </p>
                        </div>
                    </div>

                    <!-- Pillar 2 -->
                    <div class="p-7 bg-white rounded-[28px] border-2 border-slate-200 shadow-md flex items-start gap-5 flex-1">
                        <div class="w-16 h-16 rounded-2xl bg-[#9FBEED]/40 text-[#1E40AF] flex items-center justify-center flex-shrink-0">
                            <span class="material-symbols-outlined text-3xl">diversity_1</span>
                        </div>
                        <div>
                            <div class="font-black text-[#0D1B2A] text-xl mb-1.5">2. Pahami Tim Anda (Know Your Team)</div>
                            <p class="text-base text-[#475569] leading-relaxed font-semibold">
                                Pandanglah perbedaan cara berpikir bukan sebagai ancaman bagi wibawa Anda, melainkan sebagai penyeimbang yang menyelamatkan tim dari kesalahan fatal.
                            </p>
                        </div>
                    </div>

                    <!-- Pillar 3 -->
                    <div class="p-7 bg-white rounded-[28px] border-2 border-slate-200 shadow-md flex items-start gap-5 flex-1">
                        <div class="w-16 h-16 rounded-2xl bg-emerald-100 text-emerald-800 flex items-center justify-center flex-shrink-0">
                            <span class="material-symbols-outlined text-3xl">rocket_launch</span>
                        </div>
                        <div>
                            <div class="font-black text-[#0D1B2A] text-xl mb-1.5">3. Bangun Sinergi Harmonis (Build Synergy)</div>
                            <p class="text-base text-[#475569] leading-relaxed font-semibold">
                                Tim yang sukses bukanlah tim yang seluruh individunya berkarakter seragam, melainkan sebuah orkestrasi yang menyatukan ragam instrumen berbeda menjadi satu harmoni.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
    },

    # SLIDE 22: PENUTUP & KOMITMEN AKSI
    {
        "id": 22,
        "category": "PENUTUP & KOMITMEN AKSI",
        "title": "Penutup & Komitmen Aksi Bersama",
        "html": f"""
        <div class="h-full flex flex-col">
            <!-- Top Hero Container (Full Width) with PT. PP square logo -->
            <div class="bg-gradient-to-r from-[#0D1B2A] via-[#1E293B] to-[#0F172A] p-12 rounded-[36px] text-white shadow-2xl flex items-center justify-between relative overflow-hidden mb-8">
                <div class="absolute -right-12 -bottom-12 w-80 h-80 bg-[#4F90F6]/25 rounded-full blur-3xl pointer-events-none"></div>
                
                <div class="flex items-center gap-6">
                    <!-- Kotak Persegi Logo PT. PP -->
                    <div class="w-20 h-20 rounded-2xl bg-white border-2 border-slate-200 shadow-md flex items-center justify-center p-3 flex-shrink-0">
                        <img src="{logo_b64}" class="w-full h-full object-contain" alt="PT. PP Logo" />
                    </div>
                    <div>
                        <div class="inline-flex items-center gap-2.5 px-4 py-1.5 rounded-full bg-[#4F90F6]/25 border border-[#4F90F6]/40 text-[#9FBEED] font-extrabold text-xs uppercase tracking-wider mb-2">
                            <span class="material-symbols-outlined text-base">celebration</span>
                            DAPENDA GATHERING 2024 • KESIMPULAN
                        </div>
                        <h2 class="text-4xl font-black tracking-tight leading-tight mb-2">
                            Terima Kasih. <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#9FBEED] to-[#4F90F6]">Mari Bertumbuh Bersama.</span>
                        </h2>
                        <p class="text-lg text-slate-300 font-semibold leading-relaxed">
                            Satu tim, beragam kekuatan karakter alami, satu komitmen untuk kejayaan Dapenda & PT. PP.
                        </p>
                    </div>
                </div>

                <div class="w-24 h-24 rounded-[28px] bg-[#2563EB] text-white flex items-center justify-center shadow-2xl flex-shrink-0">
                    <span class="material-symbols-outlined text-5xl">handshake</span>
                </div>
            </div>

            <!-- Bottom 3 Action Commitment Bento Cards -->
            <div class="grid grid-cols-3 gap-8 flex-1">
                <!-- Action 1: Q&A -->
                <div class="bg-white p-9 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between">
                    <div>
                        <div class="w-16 h-16 rounded-2xl bg-[#4F90F6]/15 text-[#2563EB] flex items-center justify-center mb-5">
                            <span class="material-symbols-outlined text-4xl">question_answer</span>
                        </div>
                        <h3 class="text-2xl font-extrabold text-[#0D1B2A] mb-3">Sesi Diskusi & Tanya Jawab</h3>
                        <p class="text-base text-[#475569] leading-relaxed font-semibold mb-4">
                            Silakan ajukan pertanyaan atau bagikan pengalaman nyata mengenai tantangan komunikasi di unit kerja Anda.
                        </p>
                    </div>
                    <div class="inline-flex items-center gap-2 text-sm font-black text-[#2563EB]">
                        <span>Buka Forum Diskusi</span>
                        <span class="material-symbols-outlined text-lg">arrow_forward</span>
                    </div>
                </div>

                <!-- Action 2: 24h Personal Commitment -->
                <div class="bg-gradient-to-br from-white to-[#EFF6FF] p-9 rounded-[32px] border-2 border-[#4F90F6] shadow-xl flex flex-col justify-between">
                    <div>
                        <div class="w-16 h-16 rounded-2xl bg-[#2563EB] text-white flex items-center justify-center mb-5 shadow-md">
                            <span class="material-symbols-outlined text-4xl">assignment_turned_in</span>
                        </div>
                        <h3 class="text-2xl font-extrabold text-[#0D1B2A] mb-3">Komitmen 24 Jam Pertama</h3>
                        <p class="text-base text-[#334155] leading-relaxed font-semibold mb-4">
                            Pilih 1 rekan kerja yang memiliki tipe berlawanan dengan Anda. Terapkan <strong>The Platinum Rule</strong> pada rapat kerja berikutnya.
                        </p>
                    </div>
                    <div class="p-3.5 bg-white rounded-xl border border-[#9FBEED] text-sm font-black text-[#1E40AF] text-center">
                        🎯 Aksi Nyata: Kalibrasi Gaya Komunikasi
                    </div>
                </div>

                <!-- Action 3: Facilitator Details -->
                <div class="bg-white p-9 rounded-[32px] border-2 border-slate-200 shadow-md flex flex-col justify-between">
                    <div>
                        <div class="w-16 h-16 rounded-2xl bg-slate-100 text-[#475569] flex items-center justify-center mb-5">
                            <span class="material-symbols-outlined text-4xl">contact_page</span>
                        </div>
                        <h3 class="text-2xl font-extrabold text-[#0D1B2A] mb-3">Modul & Konsultasi Tim</h3>
                        <p class="text-base text-[#475569] leading-relaxed font-semibold mb-4">
                            Materi lengkap, profil tipologi unit, serta sesi coaching tim lanjutan dapat diakses melalui Divisi SDM Dapenda.
                        </p>
                    </div>
                    <div class="text-sm font-bold text-[#64748B]">
                        Dapenda Human Capital Development • 2024
                    </div>
                </div>
            </div>
        </div>
        """
    }
]

# Generate slide options for jumper menu
slides_nav_json = json.dumps([{"id": s["id"], "title": s["title"], "category": s["category"]} for s in slides])

html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Membangun Tim dengan Perspektif Kepribadian - Dapenda Gathering</title>
    
    <!-- Google Fonts: Plus Jakarta Sans -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,600&display=swap" rel="stylesheet">
    
    <!-- Google Material Symbols Outlined -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    
    <!-- Tailwind CSS (CDN) -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
                    }},
                    colors: {{
                        cloud: {{
                            whisper: '#F8FAFC',
                            surface: '#F5F6F1',
                        }},
                        misty: {{
                            sky: '#9FBEED',
                            tint: '#EAF1FB',
                        }},
                        clear: {{
                            stream: '#4F90F6',
                            vibrant: '#2563EB',
                            dark: '#1D4ED8',
                        }},
                        navy: {{
                            dark: '#0D1B2A',
                            slate: '#1E293B',
                        }}
                    }}
                }}
            }}
        }}
    </script>
    
    <style>
        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #070D18;
            margin: 0;
            padding: 0;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            width: 100vw;
            user-select: none;
        }}
        
        .material-symbols-outlined {{
            font-variation-settings: 'FILL' 0, 'wght' 500, 'GRAD' 0, 'opsz' 28;
            display: inline-block;
        }}
        
        /* 1920x1080 Full Stage Canvas */
        #stage-scaler {{
            width: 1920px;
            height: 1080px;
            position: absolute;
            transform-origin: center center;
            box-shadow: 0 35px 90px -15px rgba(0, 0, 0, 0.85);
            background: #F8FAFC;
            overflow: hidden;
            border-radius: 16px;
        }}
        
        /* Slide takes full 1080px height with generous breathing room padding */
        .slide-container {{
            width: 1920px;
            height: 1080px;
            padding: 48px 64px 48px 64px;
            box-sizing: border-box;
            display: none;
            opacity: 0;
            transition: opacity 0.25s ease-in-out;
        }}
        
        .slide-container.active {{
            display: flex;
            flex-direction: column;
            opacity: 1;
        }}
        
        /* Bullet item exact mathematical alignment */
        .bento-bullet {{
            display: grid;
            grid-template-columns: 22px 1fr;
            align-items: start;
            column-gap: 8px;
            line-height: 1.45;
        }}
        .bento-bullet .bullet-icon {{
            display: flex;
            align-items: center;
            justify-content: center;
            height: 1.45em;
            flex-shrink: 0;
        }}
        .bento-bullet .bullet-text {{
            line-height: 1.45;
            display: block;
        }}

        /* Custom scrollbar */
        ::-webkit-scrollbar {{
            width: 8px;
        }}
        ::-webkit-scrollbar-track {{
            background: #0f172a;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #4F90F6;
            border-radius: 4px;
        }}
    </style>
</head>
<body>

    <!-- 1920x1080 Scaling Master Canvas -->
    <div id="stage-scaler">
"""

# Append all slide containers
for s in slides:
    active_class = " active" if s["id"] == 1 else ""
    html_content += f"""
        <!-- SLIDE {s["id"]}: {s["title"]} -->
        <div id="slide-{s["id"]}" class="slide-container{active_class}" data-slide-id="{s["id"]}">
            {s["html"]}
        </div>
    """

html_content += f"""
        <!-- Floating Glass Minimalist HUD (Bottom-Right Floating Capsule) -->
        <!-- Takes ZERO height from the slide content, maximizing negative space & vertical breathing room -->
        <div class="absolute bottom-6 right-8 z-40 flex items-center gap-3">
            <!-- Floating Navigation Capsule -->
            <div class="flex items-center gap-3 bg-white/90 hover:bg-white backdrop-blur-md border-2 border-slate-200/90 shadow-xl rounded-full px-5 py-2.5 transition-all">
                <button id="btn-prev" class="w-9 h-9 rounded-full hover:bg-slate-100 flex items-center justify-center text-slate-800 transition" title="Slide Sebelumnya (Arrow Left)">
                    <span class="material-symbols-outlined text-2xl">chevron_left</span>
                </button>
                
                <div class="flex items-center gap-2 font-black text-sm text-[#0D1B2A] select-none px-1">
                    <span id="current-slide-num">01</span>
                    <span class="text-slate-300">/</span>
                    <span class="text-slate-400">{len(slides):02d}</span>
                </div>

                <button id="btn-next" class="w-9 h-9 rounded-full hover:bg-slate-100 flex items-center justify-center text-slate-800 transition" title="Slide Berikutnya (Arrow Right / Space)">
                    <span class="material-symbols-outlined text-2xl">chevron_right</span>
                </button>

                <div class="w-[1.5px] h-5 bg-slate-200 mx-1"></div>

                <button id="btn-grid" class="flex items-center gap-1.5 px-3 py-1.5 rounded-full hover:bg-slate-100 text-xs font-black text-[#1E293B] transition" title="Daftar Semua Slide (G)">
                    <span class="material-symbols-outlined text-lg">grid_view</span>
                    <span>Menu</span>
                </button>

                <button id="btn-fullscreen" class="w-9 h-9 rounded-full hover:bg-slate-100 flex items-center justify-center text-slate-800 transition" title="Layar Penuh (F)">
                    <span class="material-symbols-outlined text-xl">fullscreen</span>
                </button>
            </div>
        </div>

        <!-- Ultra-Thin Top Progress Line (3px) -->
        <div class="absolute top-0 left-0 right-0 h-1 bg-slate-200/60 z-30">
            <div id="progress-bar" class="h-full bg-gradient-to-r from-[#4F90F6] to-[#2563EB] transition-all duration-300" style="width: 4.54%;"></div>
        </div>

        <!-- Slide Selector Modal Drawer -->
        <div id="grid-modal" class="absolute inset-0 bg-[#0D1B2A]/90 backdrop-blur-md z-50 hidden opacity-0 transition-opacity duration-300 flex flex-col p-14">
            <div class="flex items-center justify-between pb-6 border-b-2 border-white/20 mb-8">
                <div>
                    <h3 class="text-4xl font-black text-white">Daftar Slide Presentasi</h3>
                    <p class="text-base text-slate-300 mt-1">Lompat langsung ke halaman yang diinginkan (Klik pada kartu atau tekan tombol 'G' / 'Esc' untuk menutup)</p>
                </div>
                <button id="btn-close-grid" class="w-12 h-12 rounded-2xl bg-white/10 hover:bg-white/20 text-white flex items-center justify-center transition">
                    <span class="material-symbols-outlined text-3xl">close</span>
                </button>
            </div>

            <!-- Slide Thumbnails Grid -->
            <div id="grid-cards-container" class="grid grid-cols-4 gap-5 overflow-y-auto pr-3 flex-1">
                <!-- Dynamically populated by JS -->
            </div>
        </div>
    </div>

    <!-- Interactive Navigation Scripts -->
    <script>
        const totalSlides = {len(slides)};
        let currentSlide = 1;
        const slidesMeta = {slides_nav_json};

        const stageScaler = document.getElementById('stage-scaler');
        const currentSlideNum = document.getElementById('current-slide-num');
        const progressBar = document.getElementById('progress-bar');
        const gridModal = document.getElementById('grid-modal');
        const gridContainer = document.getElementById('grid-cards-container');

        // Responsive 1920x1080 Viewport Auto-Scaling
        function resizeStage() {{
            const windowW = window.innerWidth;
            const windowH = window.innerHeight;
            const scale = Math.min(windowW / 1920, windowH / 1080);
            stageScaler.style.transform = `scale(${{scale}})`;
        }}

        window.addEventListener('resize', resizeStage);
        resizeStage();

        // Populate Slide Drawer Grid
        function populateGrid() {{
            gridContainer.innerHTML = '';
            slidesMeta.forEach(s => {{
                const card = document.createElement('div');
                card.className = `p-5 rounded-2xl border-2 transition cursor-pointer flex flex-col justify-between h-40 ${{
                    s.id === currentSlide 
                    ? 'bg-[#2563EB] text-white border-white shadow-xl ring-4 ring-blue-300/40' 
                    : 'bg-white/10 hover:bg-white/20 text-white border-white/20'
                }}`;
                card.innerHTML = `
                    <div class="flex items-center justify-between">
                        <span class="text-sm font-black px-2.5 py-0.5 rounded bg-black/30">${{String(s.id).padStart(2, '0')}}</span>
                        <span class="text-xs text-white/80 uppercase tracking-widest font-bold">${{s.category.split('•')[0]}}</span>
                    </div>
                    <div class="font-extrabold text-base leading-snug line-clamp-2">${{s.title}}</div>
                    <div class="text-xs text-white/70 font-semibold">Klik untuk membuka slide</div>
                `;
                card.addEventListener('click', () => {{
                    goToSlide(s.id);
                    toggleGridModal(false);
                }});
                gridContainer.appendChild(card);
            }});
        }}

        function toggleGridModal(show) {{
            if (show) {{
                populateGrid();
                gridModal.classList.remove('hidden');
                setTimeout(() => gridModal.classList.remove('opacity-0'), 10);
            }} else {{
                gridModal.classList.add('opacity-0');
                setTimeout(() => gridModal.classList.add('hidden'), 300);
            }}
        }}

        // Slide Switcher Function
        function goToSlide(target) {{
            if (target < 1 || target > totalSlides) return;
            
            // Hide previous active
            const prevEl = document.getElementById(`slide-${{currentSlide}}`);
            if (prevEl) prevEl.classList.remove('active');

            currentSlide = target;

            // Show new active
            const nextEl = document.getElementById(`slide-${{currentSlide}}`);
            if (nextEl) nextEl.classList.add('active');

            // Update HUD
            currentSlideNum.textContent = String(currentSlide).padStart(2, '0');
            const progress = (currentSlide / totalSlides) * 100;
            progressBar.style.width = `${{progress}}%`;
        }}

        // Event Listeners
        document.getElementById('btn-next').addEventListener('click', () => goToSlide(currentSlide + 1));
        document.getElementById('btn-prev').addEventListener('click', () => goToSlide(currentSlide - 1));
        document.getElementById('btn-grid').addEventListener('click', () => toggleGridModal(true));
        document.getElementById('btn-close-grid').addEventListener('click', () => toggleGridModal(false));

        // Fullscreen toggle
        document.getElementById('btn-fullscreen').addEventListener('click', () => {{
            if (!document.fullscreenElement) {{
                document.documentElement.requestFullscreen().catch(err => console.log(err));
            }} else {{
                document.exitFullscreen();
            }}
        }});

        // Keyboard Controls
        window.addEventListener('keydown', (e) => {{
            if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
                goToSlide(currentSlide + 1);
            }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
                goToSlide(currentSlide - 1);
            }} else if (e.key === 'Home') {{
                goToSlide(1);
            }} else if (e.key === 'End') {{
                goToSlide(totalSlides);
            }} else if (e.key.toLowerCase() === 'g') {{
                const isHidden = gridModal.classList.contains('hidden');
                toggleGridModal(isHidden);
            }} else if (e.key.toLowerCase() === 'f') {{
                if (!document.fullscreenElement) {{
                    document.documentElement.requestFullscreen().catch(() => {{}});
                }} else {{
                    document.exitFullscreen();
                }}
            }} else if (e.key === 'Escape') {{
                toggleGridModal(false);
            }}
        }});
    </script>
</body>
</html>
"""

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Presentation successfully updated: {output_file}")
print(f"Total file size: {os.path.getsize(output_file) / 1024:.1f} KB")
