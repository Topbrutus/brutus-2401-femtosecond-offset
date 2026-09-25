from decimal import Decimal, getcontext

getcontext().prec = 80

F0 = Decimal("240.1")
DELTA_T = Decimal("1e-15")

def candidate_frequency(f0: Decimal = F0, delta_t: Decimal = DELTA_T) -> Decimal:
    denominator = (Decimal(1) / f0) - delta_t
    if denominator <= 0:
        raise ValueError("The resulting period must remain positive.")
    return Decimal(1) / denominator

def main() -> None:
    f = candidate_frequency()
    delta_f = f - F0
    reconstructed = (Decimal(1) / F0) - (Decimal(1) / f)
    print(f"f0 = {F0} Hz")
    print(f"delta_T = {DELTA_T} s")
    print(f"f = {f} Hz")
    print(f"delta_f = {delta_f} Hz")
    print(f"reconstructed_delta_T = {reconstructed} s")

if __name__ == "__main__":
    main()
