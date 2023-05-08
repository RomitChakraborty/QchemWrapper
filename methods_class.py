class MethodList:
    def __init__(self):
        # Jacob's ladder
        self.rung_1 = ['spw92', 'lda', 'svwn5']
        # GGA (Generalized Gradient Approximation)
        self.rung_2 = ['b97-d3bj', 'revpbe', 'revpbe-d3bj', 'blyp', 'blyp-d3bj', 'pbe', 'bop', 'bp86', 'bp86vwn', 'bppbe', 'gam']
        # MGGA
        self.rung_3 = ['b97m-v', 'b97m-rv', 'm06-l', 'm06-l-d30', 'tpss', 'tpss-d3bj', 'revtpss', 'bloc', 'm11-l', 'mbeef', 'mgga_ms0', 'mgga_ms1', 'mgga_ms2', 'mgga_ms1-d30', 'mgga_ms2-d30', 'mgga_mvs', 'mn12-l', 'mn15-l', 'otpss', 'pkzb', 'scan', 't-hcth', 'tm', 'vsxc']
        # XX (m)GGA -- Hybrids
        self.rung_4 = ['b97', 'b97-1', 'b97-2', 'b97-3', 'b97-k', 'b1lyp', 'b1pw91', 'b3lyp5', 'wb97', 'wb97x', 'wb97x-rv', 'wb97x-v', 'wb97x-d3', 'wb97x-d', 'b3lyp-d3bj', 'revpbe0-d3bj', 'wb97m-v', 'wm05-d', 'm06-d30', 'tpssh-d3bj']
        # Double Hybrids (m)GGA
        self.rung_5 = ['dsd-pbepbe-d3', 'wb97x-2-lp', 'wb97x-2-tqz', 'xyg3', 'xygj-os', 'ptpss-d3']
        # All methods
        self.all = self.rung_1 + self.rung_2 + self.rung_3 + self.rung_4 + self.rung_5
        # Selected methods
        self.sel = ['b3lyp-d3bj', 'revpbe-d3bj', 'bp86', 'b97-d3bj', 'b97-1', 'b97-3', 'b97m-v', 'b97m-rv', 'wb97', 'wb97x', 'wb97x-d', 'wb97x-d3', 'wb97x-rv', 'wb97m-v', 'm06-l', 'm06-l-d30']
        # Geometry-optimization methods for regular use
        self.methods_geom = ['b97-d', 'wb97m-v', 'wb97x-d']

method_list = MethodList()

# Access Jacob's ladder
print(method_list.rung_1)

# Access selected methods
print(method_list.sel)

# Access geometry-optimized methods
print(method_list.methods_geom)
