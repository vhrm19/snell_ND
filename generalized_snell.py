import numpy as np


def snell(incident, normal, v1, v2):
    """
    Computes the refraction and reflection vectors of an incident ray on a surface,
    using the velocity ratio between two media (v1 and v2).

    Parameters:
    - incident: numpy array representing the incident vector [Ix, Iy, Iz].
    - normal: numpy array representing the normal vector [Nx, Ny, Nz].
    - v1: Velocity in the first medium (incident region).
    - v2: Velocity in the second medium (refracted region).

    Returns:
    - T: Refraction vector as a numpy array [Tx, Ty, Tz].
    - R: Reflection vector as a numpy array [Rx, Ry, Rz].
    """
    # Normalize the incident and normal vectors
    incident = incident / np.linalg.norm(incident)
    normal = normal / np.linalg.norm(normal)

    # Compute the velocity ratio
    h = v1 / v2

    # Compute the dot product between the normal and the incident vector
    c = -normal @ incident

    # Auxiliary constants for calculations
    omega = h * c
    ni = np.sqrt(1 + h ** 2 * (c ** 2 - 1))

    # Coefficients for refraction and reflection
    beta_refrac = -omega + np.sign(c) * ni
    beta_reflect = -omega - np.sign(c) * ni

    # Compute the refraction vector
    T = -h * incident + beta_refrac * normal

    # Compute the reflection vector
    R = -h * incident + beta_reflect * normal

    # Return the refraction and reflection vectors
    return T, R
