from decimal import Decimal, getcontext

getcontext().prec = 80

F0 = Decimal("240.1")
DELTA_T = Decimal("1e-15")
SCALE = Decimal("2401")


def candidate_frequency(f0: Decimal = F0, delta_t: Decimal = DELTA_T) -> Decimal:
    denominator = (Decimal(1) / f0) - delta_t
    if denominator <= 0:
        raise ValueError("The resulting period must remain positive.")
    return Decimal(1) / denominator


def propagated_values(
    f0: Decimal = F0,
    delta_t: Decimal = DELTA_T,
    scale: Decimal = SCALE,
) -> dict[str, Decimal]:
    f = candidate_frequency(f0, delta_t)
    delta_f = f - f0
    scaled_reference = scale * f0
    scaled_candidate = scale * f
    scaled_residual = scaled_candidate - scaled_reference
    return {
        "f": f,
        "delta_f": delta_f,
        "scaled_reference": scaled_reference,
        "scaled_candidate": scaled_candidate,
        "scaled_residual": scaled_residual,
    }


def main() -> None:
    values = propagated_values()
    reconstructed = (Decimal(1) / F0) - (Decimal(1) / values["f"])
    print(f"f0 = {F0} Hz")
    print(f"delta_T = {DELTA_T} s")
    print(f"f = {values['f']} Hz")
    print(f"delta_f = {values['delta_f']} Hz")
    print(f"scale = {SCALE}")
    print(f"scaled_reference = {values['scaled_reference']}")
    print(f"scaled_candidate = {values['scaled_candidate']}")
    print(f"scaled_residual = {values['scaled_residual']}")
    print(f"reconstructed_delta_T = {reconstructed} s")


if __name__ == "__main__":
    main()
