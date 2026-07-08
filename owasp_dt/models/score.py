from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.score_business_impact import ScoreBusinessImpact
from ..models.score_likelihood import ScoreLikelihood
from ..models.score_technical_impact import ScoreTechnicalImpact
from ..types import UNSET, Unset

T = TypeVar("T", bound="Score")


@_attrs_define
class Score:
    """
    Attributes:
        business_impact (ScoreBusinessImpact | Unset):
        business_impact_score (float | Unset):
        likelihood (ScoreLikelihood | Unset):
        likelihood_score (float | Unset):
        technical_impact (ScoreTechnicalImpact | Unset):
        technical_impact_score (float | Unset):
    """

    business_impact: ScoreBusinessImpact | Unset = UNSET
    business_impact_score: float | Unset = UNSET
    likelihood: ScoreLikelihood | Unset = UNSET
    likelihood_score: float | Unset = UNSET
    technical_impact: ScoreTechnicalImpact | Unset = UNSET
    technical_impact_score: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_impact: str | Unset = UNSET
        if not isinstance(self.business_impact, Unset):
            business_impact = self.business_impact.value

        business_impact_score = self.business_impact_score

        likelihood: str | Unset = UNSET
        if not isinstance(self.likelihood, Unset):
            likelihood = self.likelihood.value

        likelihood_score = self.likelihood_score

        technical_impact: str | Unset = UNSET
        if not isinstance(self.technical_impact, Unset):
            technical_impact = self.technical_impact.value

        technical_impact_score = self.technical_impact_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business_impact is not UNSET:
            field_dict["businessImpact"] = business_impact
        if business_impact_score is not UNSET:
            field_dict["businessImpactScore"] = business_impact_score
        if likelihood is not UNSET:
            field_dict["likelihood"] = likelihood
        if likelihood_score is not UNSET:
            field_dict["likelihoodScore"] = likelihood_score
        if technical_impact is not UNSET:
            field_dict["technicalImpact"] = technical_impact
        if technical_impact_score is not UNSET:
            field_dict["technicalImpactScore"] = technical_impact_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _business_impact = d.pop("businessImpact", UNSET)
        business_impact: ScoreBusinessImpact | Unset
        if isinstance(_business_impact, Unset):
            business_impact = UNSET
        else:
            business_impact = ScoreBusinessImpact(_business_impact)

        business_impact_score = d.pop("businessImpactScore", UNSET)

        _likelihood = d.pop("likelihood", UNSET)
        likelihood: ScoreLikelihood | Unset
        if isinstance(_likelihood, Unset):
            likelihood = UNSET
        else:
            likelihood = ScoreLikelihood(_likelihood)

        likelihood_score = d.pop("likelihoodScore", UNSET)

        _technical_impact = d.pop("technicalImpact", UNSET)
        technical_impact: ScoreTechnicalImpact | Unset
        if isinstance(_technical_impact, Unset):
            technical_impact = UNSET
        else:
            technical_impact = ScoreTechnicalImpact(_technical_impact)

        technical_impact_score = d.pop("technicalImpactScore", UNSET)

        score = cls(
            business_impact=business_impact,
            business_impact_score=business_impact_score,
            likelihood=likelihood,
            likelihood_score=likelihood_score,
            technical_impact=technical_impact,
            technical_impact_score=technical_impact_score,
        )

        score.additional_properties = d
        return score

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
